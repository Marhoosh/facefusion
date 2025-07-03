import random
from typing import Optional

import gradio

from facefusion import metadata, wording

METADATA_BUTTON : Optional[gradio.Button] = None
ACTION_BUTTON : Optional[gradio.Button] = None


def render() -> None:
	global METADATA_BUTTON
	global ACTION_BUTTON

	action = random.choice(
	[
		{
			'wording': wording.get('about.read_the_documentation'),
			'url': 'https://mp.weixin.qq.com/s/1FT3EdtWcXM3WG8enfn4VA'
		}
	])

	METADATA_BUTTON = gradio.Button(
		value = metadata.get('name') + ' ' + metadata.get('version') + ' B站主页',
		variant = 'primary',
		link = 'https://space.bilibili.com/293706477'
	)
	ACTION_BUTTON = gradio.Button(
		value = action.get('wording'),
		link = action.get('url'),
		size = 'sm'
	)
