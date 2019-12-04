#include "snake.h"

#include <SFML/Graphics.hpp>
#include <SFML/System.hpp>
#include <SFML/Window.hpp>
#include <SFML/Config.hpp>
#include <SFML/Main.hpp>
#include <unistd.h>
#include <iostream>
#include <utility>
using namespace std;

Snake::Snake(sf::RenderWindow &window, int line_nb,int column_nb)
{
  this->width=window.getSize().x/column_nb;
  this->height=window.getSize().y/line_nb;

  this->window_width=window.getSize().x;
  this->window_height=window.getSize().y;

  int starting_point_x=5*this->width;
  int starting_point_y=5*this->height;

  sf::Vertex vertex1(sf::Vector2f(starting_point_x, starting_point_y), sf::Color::Black);
  this->snake.push_back(vertex1);
  sf::Vertex vertex4(sf::Vector2f(starting_point_x+width, starting_point_y), sf::Color::Black);
  this->snake.push_back(vertex4);
  sf::Vertex vertex3(sf::Vector2f(starting_point_x+width, starting_point_y+height), sf::Color::Black);
  this->snake.push_back(vertex3);
  sf::Vertex vertex2(sf::Vector2f(starting_point_x,starting_point_y + height ), sf::Color::Black);
  this->snake.push_back(vertex2);


  sf::Vertex vertex5(sf::Vector2f(starting_point_x+width, starting_point_y), sf::Color::Red);
  this->snake.push_back(vertex5);
  sf::Vertex vertex6(sf::Vector2f(starting_point_x+2*width,starting_point_y), sf::Color::Red);
  this->snake.push_back(vertex6);
  sf::Vertex vertex7(sf::Vector2f(starting_point_x+2*width, starting_point_y+height), sf::Color::Red);
  this->snake.push_back(vertex7);
  sf::Vertex vertex8(sf::Vector2f(starting_point_x+width, starting_point_y+height), sf::Color::Red);
  this->snake.push_back(vertex8);

  cout << "Object is being created" << endl;

}

Snake::Snake(void) {
   cout << "Object is being created" << endl;
}

Snake::~Snake(void) {
   cout << "Object is being deleted" << endl;
}

void Snake::reset(sf::RenderWindow &window, int line_nb,int column_nb)
{
  this->snake.clear();
  this->food_cell.clear();

  this->width=window.getSize().x/column_nb;
  this->height=window.getSize().y/line_nb;

  this->window_width=window.getSize().x;
  this->window_height=window.getSize().y;

  int starting_point_x=5*this->width;
  int starting_point_y=5*this->height;

  sf::Vertex vertex1(sf::Vector2f(starting_point_x, starting_point_y), sf::Color::Black);
  this->snake.push_back(vertex1);
  sf::Vertex vertex4(sf::Vector2f(starting_point_x+width, starting_point_y), sf::Color::Black);
  this->snake.push_back(vertex4);
  sf::Vertex vertex3(sf::Vector2f(starting_point_x+width, starting_point_y+height), sf::Color::Black);
  this->snake.push_back(vertex3);
  sf::Vertex vertex2(sf::Vector2f(starting_point_x,starting_point_y + height ), sf::Color::Black);
  this->snake.push_back(vertex2);


  sf::Vertex vertex5(sf::Vector2f(starting_point_x+width, starting_point_y), sf::Color::Red);
  this->snake.push_back(vertex5);
  sf::Vertex vertex6(sf::Vector2f(starting_point_x+2*width,starting_point_y), sf::Color::Red);
  this->snake.push_back(vertex6);
  sf::Vertex vertex7(sf::Vector2f(starting_point_x+2*width, starting_point_y+height), sf::Color::Red);
  this->snake.push_back(vertex7);
  sf::Vertex vertex8(sf::Vector2f(starting_point_x+width, starting_point_y+height), sf::Color::Red);
  this->snake.push_back(vertex8);

}


void Snake::add_food(sf::RenderWindow &window,int food_cell_nb)
{
  for (int i=0;i<food_cell_nb;i++)
  {
    int x = rand() % window.getSize().x/this->width;
    int y = rand() % window.getSize().y/this->height;

    // cout<<x<<y<<endl;
    sf::Vertex vertex1(sf::Vector2f(x*this->width, y*this->height), sf::Color::Green);
    this->food_cell.push_back(vertex1);
    sf::Vertex vertex4(sf::Vector2f(x*this->width+width, y*this->height), sf::Color::Green);
    this->food_cell.push_back(vertex4);
    sf::Vertex vertex3(sf::Vector2f(x*this->width+width, y*this->height+height), sf::Color::Green);
    this->food_cell.push_back(vertex3);
    sf::Vertex vertex2(sf::Vector2f(x*this->width,y*this->height + height ), sf::Color::Green);
    this->food_cell.push_back(vertex2);
  }
}



void Snake::get_position()
{
  cout<<this->snake[0].position.x/this->width<<" "<<this->snake[0].position.y/this->height<<endl;
}


int Snake::get_size()
{
  return this->snake.size();
}

void Snake::draw(sf::RenderWindow &window)
{
  window.draw(&this->food_cell[0],this->food_cell.size(), sf::Quads);
  window.draw(&this->snake[0],this->snake.size(), sf::Quads);
  window.display();
}

void Snake::go_left()
{
  for (int i=0;i<4;i++)
  {
    sf::Vertex vertex(sf::Vector2f(this->snake[3].position.x-this->width,this->snake[3].position.y), sf::Color::Black);
    this->snake.insert(this->snake.begin(),vertex);
  }
  for (int i=0;i<4;i++)
  {
    this->snake.pop_back();
  }
  if(this->snake.size()>4)
  {
    for (int i=4;i<this->snake.size();i++)
    {
      this->snake[i].color=sf::Color::Red;
    }
  }
}

void Snake::go_right()
{

  for (int i=0;i<4;i++)
  {
    sf::Vertex vertex(sf::Vector2f(this->snake[3].position.x+this->width,this->snake[3].position.y), sf::Color::Black);
    this->snake.insert(this->snake.begin(),vertex);
  }
  for (int i=0;i<4;i++)
  {
    this->snake.pop_back();
  }
  if(this->snake.size()>4)
  {
    for (int i=4;i<this->snake.size();i++)
    {
      this->snake[i].color=sf::Color::Red;
    }
  }
}

void Snake::go_up()
{
  for (int i=0;i<4;i++)
  {
    sf::Vertex vertex(sf::Vector2f(this->snake[3].position.x,this->snake[3].position.y-this->height), sf::Color::Black);
    this->snake.insert(this->snake.begin(),vertex);
  }
  for (int i=0;i<4;i++)
  {
    this->snake.pop_back();
  }
  if(this->snake.size()>4)
  {
    for (int i=4;i<this->snake.size();i++)
    {
      this->snake[i].color=sf::Color::Red;
    }
  }
}

void Snake::go_down()
{
  for (int i=0;i<4;i++)
  {
    sf::Vertex vertex(sf::Vector2f(this->snake[3].position.x,this->snake[3].position.y+this->height), sf::Color::Black);
    this->snake.insert(this->snake.begin(),vertex);
  }
  for (int i=0;i<4;i++)
  {
    this->snake.pop_back();
  }
  if(this->snake.size()>4)
  {
    for (int i=4;i<this->snake.size();i++)
    {
      this->snake[i].color=sf::Color::Red;
    }
  }
}


void Snake::eat()
{
  sf::Vertex vertex1(this->snake[snake.size()-4].position, sf::Color::Red);
  this->snake.push_back(vertex1);
  sf::Vertex vertex2(this->snake[snake.size()-3].position, sf::Color::Red);
  this->snake.push_back(vertex2);
  sf::Vertex vertex3(this->snake[snake.size()-2].position, sf::Color::Red);
  this->snake.push_back(vertex3);
  sf::Vertex vertex4(this->snake[snake.size()-1].position, sf::Color::Red);
  this->snake.push_back(vertex4);
}

bool Snake::is_on_food_cell()
{
  vector<int> snake_coord,food_cell_coord;

  if (this->food_cell.size()==0)
  {
    return false;
  }

  for (int i=0;i<4;i++)
  {
    snake_coord.push_back(this->snake[i].position.x);
    snake_coord.push_back(this->snake[i].position.y);

  }
  for (int i=0;i<this->food_cell.size()-3;i+=4)
  {
    food_cell_coord.clear();
    for(int j=i;j<i+4;j++)
    {
      food_cell_coord.push_back(this->food_cell[j].position.x);
      food_cell_coord.push_back(this->food_cell[j].position.y);
    }
    if (snake_coord==food_cell_coord)
    {
      this->food_cell.erase(this->food_cell.begin()+i,this->food_cell.begin()+i+4);
      return true;
    }
  }
  return false;
}


bool Snake::is_dead()
{
  for (int i=0;i<4;i++)
  {
    if (this->snake[i].position.x<0 || this->snake[i].position.x>this->window_width)
    {
      return true;
    }
    else if(this->snake[i].position.y<0 || this->snake[i].position.y>this->window_height)
    {
      return true;
    }
  }

  if (this->snake.size()<5)
  {
    return false;
  }

  vector<int> snake_head,snake_body;

  for (int i=0;i<4;i++)
  {
    snake_head.push_back(this->snake[i].position.x);
    snake_head.push_back(this->snake[i].position.y);

  }
  for (int i=4;i<this->snake.size()-3;i+=4)
  {
    snake_body.clear();
    for(int j=i;j<i+4;j++)
    {
      snake_body.push_back(this->snake[j].position.x);
      snake_body.push_back(this->snake[j].position.y);
    }
    if (snake_head==snake_body)
    {
      return true;
    }
  }
  return false;
}
