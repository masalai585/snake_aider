document.addEventListener("DOMContentLoaded", () => {
    const gameBoard = document.getElementById("game-board");
    const gridSize = 20;
    const gridWidth = gameBoard.offsetWidth / gridSize;
    const gridHeight = gameBoard.offsetHeight / gridSize;
    const snake = [{ x: 0, y: 0 }];
    let food = { x: 0, y: 0 };
    let dx = 1;
    let dy = 0;
    let score = 0;
    let gameLoop;

    function createSnake() {
        snake.forEach(segment => {
            const snakeElement = document.createElement("div");
            snakeElement.style.gridColumnStart = segment.x + 1;
            snakeElement.style.gridRowStart = segment.y + 1;
            snakeElement.classList.add("snake");
            gameBoard.appendChild(snakeElement);
        });
    }

    function createFood() {
        food = {
            x: Math.floor(Math.random() * gridWidth),
            y: Math.floor(Math.random() * gridHeight)
        };

        const foodElement = document.createElement("div");
        foodElement.style.gridColumnStart = food.x + 1;
        foodElement.style.gridRowStart = food.y + 1;
        foodElement.classList.add("food");
        gameBoard.appendChild(foodElement);
    }

    function moveSnake() {
        const head = { x: snake[0].x + dx, y: snake[0].y + dy };
        snake.unshift(head);

        if (head.x === food.x && head.y === food.y) {
            score++;
            createFood();
        } else {
            snake.pop();
        }

        if (head.x < 0 || head.x >= gridWidth || head.y < 0 || head.y >= gridHeight || checkCollision()) {
            gameOver();
        }

        updateGameBoard();
    }

    function updateGameBoard() {
        const snakeElements = document.querySelectorAll(".snake");
        snakeElements.forEach(element => element.remove());

        const foodElement = document.querySelector(".food");
        foodElement.remove();

        createSnake();
        createFood();
    }

    function checkCollision() {
        const head = snake[0];
        return snake.slice(1).some(segment => segment.x === head.x && segment.y === head.y);
    }

    function changeDirection(event) {
        const keyPressed = event.keyCode;
        const isMovingUp = dy === -1;
        const isMovingDown = dy === 1;
        const isMovingLeft = dx === -1;
        const isMovingRight = dx === 1;

        if (keyPressed === 37 && !isMovingRight) {
            dx = -1;
            dy = 0;
        }

        if (keyPressed === 38 && !isMovingDown) {
            dx = 0;
            dy = -1;
        }

        if (keyPressed === 39 && !isMovingLeft) {
            dx = 1;
            dy = 0;
        }

        if (keyPressed === 40 && !isMovingUp) {
            dx = 0;
            dy = 1;
        }
    }

    function startGame() {
        clearInterval(gameLoop);
        snake.length = 1;
        dx = 1;
        dy = 0;
        score = 0;
        createSnake();
        createFood();
        gameLoop = setInterval(moveSnake, 200);
    }

    function gameOver() {
        clearInterval(gameLoop);
        alert("Game Over! Your score: " + score);
        startGame();
    }

    createSnake();
    createFood();
    startGame();
    document.addEventListener("keydown", changeDirection);
});
