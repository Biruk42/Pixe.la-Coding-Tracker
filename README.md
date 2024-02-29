# Pixe.la Coding Tracker

## Overview
This Python script interacts with the Pixe.la API to track coding activities. It allows you to create a graph to visualize your coding progress over time.

## Requirements
- Python 3.x
- `requests` library

## Configuration
1. Obtain your Pixe.la username and token from the Pixe.la website.
2. Update the `USERNAME` and `TOKEN` variables in the script with your Pixe.la username and token.
3. Define a `GRAPH_ID` for your graph (e.g., "graph1").

## Usage
1. Run the script.
2. Follow the prompts to input the quantity of time you spent coding.
3. The script will create a new pixel on your Pixe.la graph representing the time you spent coding today.

## API Endpoints
- `pixela_endpoint`: The base URL for Pixe.la API requests.
- `graph_endpoint`: The endpoint to create a new graph.
- `pixel_creation_endpoint`: The endpoint to create a new pixel on the graph for today's date.
- `update_endpoint`: The endpoint to update the quantity of an existing pixel for today's date.
- `delete_endpoint`: The endpoint to delete a pixel for today's date.

## Note
- Ensure that your Pixe.la account has been set up and that you have agreed to the terms of service.
- Make sure to provide a meaningful `GRAPH_ID` to uniquely identify your graph.

## Disclaimer
This script is for educational purposes only. Use it responsibly and ensure compliance with Pixe.la's terms of service.

## Contributions
Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or create a pull request.
