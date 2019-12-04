#include <SFML/Graphics.hpp>
#include <SFML/System.hpp>
#include <SFML/Window.hpp>
#include <SFML/Config.hpp>
#include <SFML/Main.hpp>
#include <unistd.h>
#include <iostream>
#include <stdlib.h>

#include "snake.h"

using namespace std;
void print(string x){cout<<x<<endl;}


int main(int argc, char *argv[])
{

    int width=800;
    int height=800;
    int level=1;
    try
    {
      if(argc>1)
      {
        level=atoi(argv[1]);
        if(level>5)
        {
          print("Trust me, you're in deep shit");
        }
        if(level>20)
        {
          print("Max level is 20");
          print("Trust me, you're in deep shit");
        }
      }
    }
    catch(int e)
    {
      cout<<"Erreur de conversion"<<endl;
    }

    sf::RenderWindow window(sf::VideoMode(width, height), "Snake");

    sf::Texture background;
    if (!background.loadFromFile("white_square.png"))
        return EXIT_FAILURE;
    sf::Sprite sprite(background);
    sprite.setTexture(background);

    sf::Image image_menu;
    image_menu.create(width, height,sf::Color(0, 153, 0));
    sf::Font font;
    font.loadFromFile("arial.ttf");
    sf::Text text("This is Snake", font);
    sf::Text text2("Press enter to play",font);

    text.setCharacterSize(50);
    text.setStyle(sf::Text::Bold);
    text.setColor(sf::Color(0, 53, 0));
    sf::FloatRect textRect = text.getLocalBounds();
    text.setOrigin(textRect.left + textRect.width/2.0f,
               textRect.top  + textRect.height/2.0f);
    text.setPosition(sf::Vector2f(width/2.0f,height/2.0f));

    text2.setCharacterSize(50);
    text2.setStyle(sf::Text::Bold);
    text2.setColor(sf::Color(0, 53, 0));
    sf::FloatRect textRect2 = text2.getLocalBounds();
    text2.setOrigin(textRect2.left + textRect2.width/2.0f,
               textRect2.top  + textRect2.height/2.0f);
    text2.setPosition(sf::Vector2f(width/2.0f,height/1.5f));

    sf::Texture texture_menu;
    texture_menu.loadFromImage(image_menu);
    sf::Sprite sprite_menu(texture_menu);
    window.clear();

    Snake lala(window,10,10);
    int score=0;
    bool first_game=true;
    int num_event=0;

    // window.setActive();
    // window.setVerticalSyncEnabled(true);
    // window.setFramerateLimit(30);

    while (window.isOpen())
    {
        sf::Event event;
        while (first_game)
        {
          // cout<<first_game<<endl;
          if(sf::Keyboard::isKeyPressed(sf::Keyboard::Return))
          {
            first_game=false;
            lala.reset(window,20,20);
            lala.add_food(window,1);
            window.clear();
            score=0;
            break;
          }
          window.clear();
          window.draw(sprite_menu);
          window.draw(text);
          window.draw(text2);
          window.display();
        }
        // sf::Event event;
        while (!first_game && window.pollEvent(event) or num_event!=0)
        {
            if (event.type == sf::Event::Closed)
                window.close();
            else if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left))
            {
              lala.go_left();
              num_event=1;
            }
            else if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right))
            {
              lala.go_right();
              num_event=2;
            }
            else if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up))
            {

                lala.go_up();
                num_event=3;
            }
            else if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down))
            {

                lala.go_down();
                num_event=4;
            }
            else if(num_event==1)
            {
              lala.go_left();
            }
            else if (num_event==2)
            {
              lala.go_right();
            }
            else if (num_event==3)
            {
              lala.go_up();
            }
            else if (num_event==4)
            {
              lala.go_down();
            }

            if (lala.is_dead())
            {
              cout<<"You'r dead"<<endl;
              first_game=true;
              num_event=0;
              cout<<"Score : "<<score<<endl;
              break;
            }
            else if (lala.is_on_food_cell())
            {
              lala.eat();
              lala.add_food(window,1);
              score++;
            }
            window.clear();
            window.draw(sprite);
            lala.draw(window);
            window.display();
            usleep(50000-level*1000*score);
        }
        // window.draw(sprite);
        // lala.draw(window);
        // window.draw(sprite);
        // lala.draw(window);
    }

    return 0;
}
