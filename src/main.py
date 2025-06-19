import os
from camel.types.enums import ModelType
import google.generativeai as genai
import googlemaps
import yaml
from camel.agents import ChatAgent
from camel.types import RoleType
from camel.societies import RolePlaying
from camel.configs.openai_config import ChatGPTConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.messages import BaseMessage
from camel.agents import ChatAgent
from dotenv import load_dotenv
from GoogleMapsAgent import GoogleMapsAgent
import json

load_dotenv()

# model = ModelFactory.create(
#     model_platform=ModelPlatformType.GEMINI,
#     model_type=ModelType.GEMINI_2_0_PRO_EXP,
#     model_config_dict={}
# )

# # Step 2: Prepare the system message
# system_msg = BaseMessage.make_assistant_message(
#     role_name="MedicalExpert",
#     content="You are a helpful medical expert focusing on hospital recommendations."
# )

# # Step 3: Instantiate the ChatAgent with the model
# gemini_agent = ChatAgent(
#     system_message=system_msg,
#     model=model,
# )

maps_agent = GoogleMapsAgent()

latitude = 17.4669416
longitude = 78.3631222
address = maps_agent.get_address(latitude, longitude)

res = maps_agent.find_hospitals("Chest Pain", address)

print(json.dumps(res, indent=3))


# disease = "Dengue"
# latitude = 17.4669416, longitude = 78.3631222

# task_prompt = f"Find best hospitals in {city} for treating {disease}."

# role_play = RolePlaying(
#     task_prompt=f"Find best hospitals in {city} for {disease}.",
#     assistant_role_name="MedicalExpert",
#     user_role_name="HospitalLocator",
#     with_task_specify=True,
# )

# assistant_msg = role_play.init_chat()
# print(f"\n🧠 Gemini: {assistant_msg.content}")

# msg = role_play.step(assistant_msg=assistant_msg)

# print(msg)

# maps_results = maps_agent.find_hospitals(disease, city)
# print("\n📍 Google Maps:")
# for res in maps_results:
#     print(f" - {res}")