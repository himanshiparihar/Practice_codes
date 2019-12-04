#include <SFML/Window.hpp>
#include <SFML/Graphics.hpp>
#include <SFML/System.hpp>
#include <vector>


sf::Event event;
enum Direction { Up, Down, Left, Right};
int dir = Up;

class SnakeBlock
{
    public:

    SnakeBlock * next;
    sf::Texture texture;
    sf::Sprite snakeblock;
};

int main()
{
    sf::Sprite background;
    sf::Texture backgroundtex;
    backgroundtex.loadFromFile("background.png", sf::IntRect(0, 0, 1987, 1315));
    background.setTexture(backgroundtex);

    SnakeBlock snakeHead;
    snakeHead.texture.loadFromFile("spritesheetsnake.png", sf::IntRect(0,0,52,44));
    snakeHead.snakeblock.setTexture(snakeHead.texture);

    std::vector<SnakeBlock> Snake;
    Snake.push_back(snakeHead);
    Snake[0].snakeblock.setPosition(100,100);

    sf::RenderWindow window(sf::VideoMode(800,600), "SFML Snake");
    window.setFramerateLimit(30);
    while(window.isOpen())
    {
        while(window.pollEvent(event))
        {
            switch(event.type)
            {
                case sf::Event::Closed:

                window.close();
                break;

                default:
                break;
            }

        }

        if(sf::Keyboard::isKeyPressed(sf::Keyboard::Left))
        {
                dir = Left;
        }
        if(sf::Keyboard::isKeyPressed(sf::Keyboard::Right))
        {
                dir = Right;
        }
        if(sf::Keyboard::isKeyPressed(sf::Keyboard::Down))
        {
                dir = Down;
        }
        if(sf::Keyboard::isKeyPressed(sf::Keyboard::Up))
        {
                dir = Up;
        }
        while(dir == Up)
        {
            Snake[0].snakeblock.move(0,-5);
        }
        while(dir == Down)
        {
            Snake[0].snakeblock.move(0,5);
        }
        while(dir == Left)
        {
            Snake[0].snakeblock.move(-5,0);
        }
        while(dir == Right)
        {
            Snake[0].snakeblock.move(5,0);
        }
        window.clear(sf::Color::Green);

        window.draw(background);
        window.draw(Snake[0].snakeblock);

        window.display();
    }
    return 0;
}
