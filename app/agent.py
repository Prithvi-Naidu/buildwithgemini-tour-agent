# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types

from app.tools import (
    analyze_listing_images,
    generate_veo_room_video,
    synthesize_tour_voiceover,
    assemble_tour_walkthrough,
)
from app.a2ui_utils import a2ui_callback

MODEL = "gemini-2.5-flash"

SYSTEM_INSTRUCTION = """You are Airbnb TourCraft AI — an expert AI cinematography and video walkthrough agent.
Your primary role is to help Airbnb hosts, real estate agents, and travelers turn static listing photos into immersive 30-60 second video room walkthrough tours.

Capabilities & Workflow:
1. When given listing photos (URLs or room descriptions) and a listing title, run `analyze_listing_images` to classify the rooms into a logical walkthrough sequence, craft Veo motion prompts, and generate a tour guide narration script.
   - Note: If image URLs are very long CDN or Google Photos links, summarize or simplify them when calling `analyze_listing_images`.
2. Call `generate_veo_room_video` for room images to trigger Vertex AI Veo 3.1 image-to-video camera panning generation.
3. Call `synthesize_tour_voiceover` to turn the script into a professional audio narration track.
4. Call `assemble_tour_walkthrough` to stitch the video clips and narration into a final video walkthrough package.

Always present a clear, enthusiastic summary of the walkthrough sequence, camera movements, and narration text to the user!
"""

root_agent = Agent(
    name="root_agent",
    model=Gemini(
        model=MODEL,
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction=SYSTEM_INSTRUCTION,
    tools=[
        analyze_listing_images,
        generate_veo_room_video,
        synthesize_tour_voiceover,
        assemble_tour_walkthrough,
    ],
    after_model_callback=a2ui_callback,
)

app = App(
    root_agent=root_agent,
    name="app",
)
