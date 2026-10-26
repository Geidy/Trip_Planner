import os
from openai import OpenAI

# Define the model to use
model = "gpt-4o-mini"

# Define the client
client = openai.OpenAI(api_key=api_key)

# Define the messages list correctly (as a list of dicts)
conversation = [
     {"role": "system",
     "content": "You are a Top Parisian travel expert"},
    {"role": "user",
     "content": "Could you please help me plan my trip to Paris"},
    {"role": "assistant",
     "content": "You will be able to advise and find the best attractions. You have the ability to plan an itinerary of 2 - 3 activities within the day. "
     "Please take into account: prices, distance from each other, weather. Example: Eiffel Tower, Louvre Museum, Arc de Triomphe. "
     "Please keep in mind adventures or day trips to nearby hidden locations."},
    {"role": "user", 
     "content": "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving"},
    {"role": "user",
     "content": "Where is the Arc de Triomphe"},
    {"role": "user",
     "content": "What are the must-see artworks at the Lovre Museum?"}
]

# FIX: Concatenate the system message and conversation lists properly
#messages = [{"role": "system", "content": "You are a Top Parisian travel expert."}] + conversation

for i in range(len(conversation)):
    if conversation[i]['role'] == 'user':
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation[:i+1],
            temperature=0.0,
            max_tokens=1000
        )
        conversation[i]['response'] = response.choices[0].message.content
        print(f"Assistant: {conversation[i]['response']}")

        
