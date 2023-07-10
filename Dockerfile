# Use a base Python image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the game files into the container
COPY snake_game.py /app/

# Install the required dependencies
RUN pip install pygame pgzero

# Set the command to run the game
CMD ["python", "snake_game.py"]
