import os
import io
import base64
import json

import openai



class AdventureManager:
	# low + square = 272 tokens (minimum).
	def __init__(
		self, img_gen_model='gpt-image-1', img_quality='low',
		img_size='1024x1024', img_fmt='webp', img_compression=None,
		output_path='output', user=None, sys_msg=''
	):
		self.img_gen_model = img_gen_model
		self.img_quality = img_quality
		self.img_size = img_size
		self.img_fmt = img_fmt
		self.img_compression = img_compression
		self.output_path = output_path
		if self.output_path:
			os.makedirs(output_path, exist_ok=True)
		
		self.global_sys_msg = sys_msg
		
		self.user = user
		self.ai = openai.Client(api_key=os.environ.get('OPENAI_API_KEY'))


	def get_img(self, response):
		img_b64 = response.data[0].b64_json
		return base64.b64decode(img_b64)
	

	def img_to_bin(self, img):
		binary = io.BytesIO(img)
		binary.seek(0)
		# Set 'name' on the binary so the openai library doesn't use
		# a name without extension, as it would cause the API to
		# reject the file.
		binary.name = f'tmp.{self.img_fmt}'
		return binary
	

	def load_img(self, path):
		with open(path, 'rb') as file:
			return file.read()
	

	def save_img(self, name, img_bytes):
		path = os.path.join(self.output_path, f'{name}.{self.img_fmt}')
		with open(path, 'wb') as file:
			file.write(img_bytes)
		return path


	def gen_img(self, prompt, sys_msg=None):
		# TODO - System messages are seemingly not supported.
		sys_msg = sys_msg or\
			"""This is some kind of textual adventure, the user is the player,
			you are the game manager. The adventure just started, generate
			an image based on the given area description."""
		
		response = self.ai.images.generate(
			model=self.img_gen_model,
			quality=self.img_quality,
			size=self.img_size,
			output_format=self.img_fmt,
			output_compression=self.img_compression,
			user=self.user,

			prompt=prompt
		)

		return self.get_img(response)


	def edit_img(self, img, prompt, sys_msg=None):
		"""img must be a file."""

		# TODO - System messages are seemingly not supported.
		sys_msg = sys_msg or\
			"""This is some kind of textual adventure, the user is the player,
			you are the game manager. The player just entered a previously
			visited area, edit the image based on what the player's willings."""
		
		if isinstance(img, bytes):
			img = self.img_to_bin(img)

		response = self.ai.images.edit(
			model=self.img_gen_model,
			quality=self.img_quality,
			size=self.img_size,
			extra_body={
				'output_format': self.img_fmt,
				'output_compression': self.img_compression,
			},
			user=self.user,
			
			image=img,
			prompt=prompt
		)

		return self.get_img(response)