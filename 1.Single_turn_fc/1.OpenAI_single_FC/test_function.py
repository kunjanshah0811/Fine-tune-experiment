from openai import OpenAI
import json, os
from secret_key import openai_api_key

client = OpenAI(api_key=openai_api_key)

# 1 Your callable Python function
def get_current_weather(location:str, unit:str='fahrenheit'):
    
    weather_info = {"location": location, "unit": unit,
         "temperature": 75, "forecast": ["windy", "sunny"]}
    
    return json.dumps(weather_info)  # return a JSON string   

def get_humidity(location: str):
    return json.dumps({"location": location, "humidity": "60%"})

def get_wind_speed(location: str):
    return json.dumps({"location": location, "wind_speed": "12 km/h"})

def get_uv_index(location: str):
    return json.dumps({"location": location, "uv_index": 5})

def get_air_quality(location: str):
    return json.dumps({"location": location, "aqi": 42})

def get_sunrise_sunset(location: str):
    return json.dumps({"location": location, "sunrise": "06:00", "sunset": "18:30"})

def get_precipitation(location: str):
    return json.dumps({"location": location, "precipitation": "0.2 mm"})

def get_pressure(location: str):
    return json.dumps({"location": location, "pressure": "1013 hPa"})

def get_visibility(location: str):
    return json.dumps({"location": location, "visibility": "10 km"})

def get_cloud_cover(location: str):
    return json.dumps({"location": location, "cloud_cover": "25%"})

def get_humidity(location: str):
    return json.dumps({"location": location, "humidity": "60%"})

def get_wind_speed(location: str):
    return json.dumps({"location": location, "wind_speed": "12 km/h"})

def get_uv_index(location: str):
    return json.dumps({"location": location, "uv_index": 5})

def get_air_quality(location: str):
    return json.dumps({"location": location, "aqi": 42})

def get_sunrise_sunset(location: str):
    return json.dumps({"location": location, "sunrise": "06:00", "sunset": "18:30"})

def get_precipitation(location: str):
    return json.dumps({"location": location, "precipitation": "0.2 mm"})

def get_pressure(location: str):
    return json.dumps({"location": location, "pressure": "1013 hPa"})

def get_visibility(location: str):
    return json.dumps({"location": location, "visibility": "10 km"})

def get_cloud_cover(location: str):
    return json.dumps({"location": location, "cloud_cover": "25%"})


tools = []
for func in [
    get_current_weather, get_humidity, get_wind_speed, get_uv_index,
    get_air_quality, get_sunrise_sunset, get_precipitation,
    get_pressure, get_visibility, get_cloud_cover
]:
    tools.append({
        "type": "function",
        "name": func.__name__,
        "description": func.__doc__ or f"Call the `{func.__name__}` function",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string"}
            },
            "required": ["location"]
        }
    })

messages = [ {"role": "system", "content": f"You are a helpful assistant that can call any number of functions."},
    {"role": "user", "content": "Is it still foggy in Seattle, and what’s the uv risk for people heading to beaches in Miami tomorrow?"}]

response = client.responses.create( 
    model="o4-mini-2025-04-16",        # or any tool-calling-capable model
    input=messages,
    tools=tools,                # attach the schema
    tool_choice="auto",
    parallel_tool_calls=True   # let the model decide
)

# 3️⃣ Extract and print all tool calls
for tool_call in response.output:
    print("Tool Call:", tool_call)


result = [
    {
        "type": tool_call.type,
        "id": tool_call.id,
        "call_id": tool_call.call_id,
        "name": tool_call.name,
        "arguments": tool_call.arguments
    }
    for tool_call in response.output
    if getattr(tool_call, "type", None) == "function_call"
]

print(json.dumps(result, indent=4))               
#print(tool_call.function.name)        
#print(tool_call.function.arguments)   


# Parse arguments from the tool call (they are a JSON string)
#args = json.loads(tool_call.arguments) # {"location": "India", "unit": "fahrenheit"}
# Call the function with the parsed arguments
available_functions = {
    'get_current_weather': get_current_weather,
    'get_humidity': get_humidity,
    'get_wind_speed': get_wind_speed,
    'get_uv_index': get_uv_index,
    'get_air_quality': get_air_quality,
    'get_sunrise_sunset': get_sunrise_sunset,
    'get_precipitation': get_precipitation,
    'get_pressure': get_pressure,
    'get_visibility': get_visibility,
    'get_cloud_cover': get_cloud_cover
}

# Loop through all tool calls for parallel execution
for tool_call in response.output:
    if getattr(tool_call, "type", None) == "function_call":
        args = json.loads(tool_call.arguments)
        function_to_call = available_functions[tool_call.name]
        function_result = function_to_call(**args)
        print(f"Function '{tool_call.name}' response:", function_result)