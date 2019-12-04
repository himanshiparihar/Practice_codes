#include <SFML/Graphics.hpp>
#include <SFML/System.hpp>
#include <SFML/Window.hpp>
#include <SFML/Config.hpp>
#include <SFML/Main.hpp>
#include <unistd.h>
#include <iostream>
using namespace std;



class Snake
{
public:
    Snake();
    Snake(sf::RenderWindow &window, int line_nb,int column_nb);
    ~Snake();
    void eat();
    int get_size();
    void draw(sf::RenderWindow &window);
    void go_left();
    void go_right();
    void go_up();
    void go_down();
    bool is_dead();
    bool is_on_food_cell();
    void get_position();
    void add_food(sf::RenderWindow &window,int food_cell_nb);
    void reset(sf::RenderWindow &window, int line_nb,int column_nb);

private:
    vector<sf::Vertex> snake;
    vector<sf::Vertex> food_cell;
    int width;
    int height;
    int window_width;
    int window_height;
};
