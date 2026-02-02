"""
Weather information fetcher tool.
Note: This is a mock implementation. In a real scenario, you would integrate with a weather API.
"""

from agents import function_tool


@function_tool
def weather_fetcher(location: str) -> str:
    """
    Fetch current weather information for a given location.
    
    Args:
        location: The city or location to get weather for (e.g., "New York", "London", "Tokyo").
        
    Returns:
        Current weather information for the specified location.
    """
    # This is a mock implementation
    # In a real scenario, you would integrate with a weather API like OpenWeatherMap
    
    location = location.strip()
    if not location:
        return "Error: No location specified."
    
    # Mock weather data based on location with more realistic and varied data
    mock_weather_data = {
        "new york": "🌤️ Partly cloudy, 22°C (72°F), Humidity: 65%, Wind: 8 mph from the west",
        "london": "☁️ Overcast, 15°C (59°F), Humidity: 78%, Wind: 12 mph from the south",
        "tokyo": "🌤️ Partly cloudy, 18°C (64°F), Humidity: 55%, Wind: 5 mph calm conditions",
        "paris": "🌧️ Light rain, 16°C (61°F), Humidity: 82%, Wind: 10 mph from the north",
        "sydney": "☀️ Clear skies, 25°C (77°F), Humidity: 45%, Wind: 6 mph from the east",
        "berlin": "🌦️ Light drizzle, 14°C (57°F), Humidity: 70%, Wind: 7 mph from the northwest",
        "madrid": "☀️ Sunny, 28°C (82°F), Humidity: 40%, Wind: 4 mph light breeze",
        "moscow": "❄️ Snow flurries, -5°C (23°F), Humidity: 85%, Wind: 15 mph from the northeast",
        "dubai": "☀️ Clear, 32°C (90°F), Humidity: 25%, Wind: 3 mph light winds",
        "mumbai": "🌧️ Heavy rain, 26°C (79°F), Humidity: 90%, Wind: 18 mph from the southwest"
    }
    
    location_lower = location.lower()
    
    # Check for exact matches first
    if location_lower in mock_weather_data:
        return f"Weather in {location}: {mock_weather_data[location_lower]}"
    
    # Check for partial matches
    for city, weather in mock_weather_data.items():
        if city in location_lower or location_lower in city:
            return f"Weather in {location}: {weather}"
    
    # Default response for unknown locations
    return f"Weather information for {location}: Partly cloudy, 20°C (68°F), Light winds. (Note: This is mock data - integrate with a real weather API for actual data)"
