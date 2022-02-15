/*
Student Name: Jacob Gowan
Student NetID: jag1065
Compiler Used: Visual Studio
Program Description:
This program manages simulates
*/

#include "Hash.h"
#include "User.h"
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <iostream>

using std::cin;
using std::cout;
using std::endl;
using std::fstream;
using std::istream;
using std::ios;
using std::ios_base;
using std::string;
using std::stringstream;
using std::stoi;
using std::ofstream;

bool getWord(istream& is, string& s)
{
    if (getline(is, s, ' ')) return true;
    return false;
}

bool skipWord(istream& is)
{
    string s;
    if (getline(is, s, ' ')) return true;
    return false;
}

bool parseStream(istream& is, bool interactive = true)
{
    string str;
    string command;
    string value;
    string value2;
    hash hashTable(23);
    bool tf;

    while (true)
    {
        cout << endl;
        if (interactive) { cout << ">> "; }
        else
            if (is.eof()) { return true; }

        getline(is, str);
        stringstream ss(str);

        getWord(ss, command);

        // EXIT ////////////////////////////////////////////////////////////////////////////////////

        if (command == "exit")
        {
            break;
        }

        // LOAD ////////////////////////////////////////////////////////////////////////////////////

        else if (command == "load")
        {
            getWord(ss, value);
            if (value == "pwd")
            {
                getWord(ss, value2);
                hashTable.loadTable(value2);
            }
            else
            {
                std::ifstream is;
                is.open(value);
                if (is.is_open())
                {
                    parseStream(is, false);
                }
                is.close();
            }
            continue;
        }

        // SAVE ////////////////////////////////////////////////////////////////////////////////////

        else if (command == "save")
        {
            skipWord(ss);
            getWord(ss, value);
            hashTable.saveTable(value);
            continue;
        }

        // NEW /////////////////////////////////////////////////////////////////////////////////////

        else if (command == "new")
        {
            getWord(ss, value);
            getWord(ss, value2);
            string id = value;
            string pass = value2;
            string directory = "/user/" + id;
            hashTable.insertItem(id, directory, pass);
            continue;
        }

        // REMOVE //////////////////////////////////////////////////////////////////////////////////

        else if (command == "remove")
        {
            getWord(ss, value);
            string id = value;
            tf =hashTable.deleteItem(id);
            if (tf == true)
            {
                cout << "Removed successfully." << endl;
            }
            else
            {
                cout << "Failed to remove. Please try again." << endl;
            }
            continue;
        }

        // CLEAR ///////////////////////////////////////////////////////////////////////////////////

        else if (command == "clear")
        {
            hashTable.clear();
            continue;
        }

        // DISPLAY /////////////////////////////////////////////////////////////////////////////////

        else if (command == "display")
        {
            
            if (getWord(ss, value))
            {
                string id = value;
                tf = hashTable.userDisplay(id);
                if (tf == false)
                {
                    cout << "Failed to display. Please try again." << endl;
                }
            }
            else
            {
                hashTable.display();
            }
            continue;
        }

        // VERIFY ///////////////////////////////////////////////////////////////////////////////////////

        else if (command == "verify")
        {
            getWord(ss, value);
            getWord(ss, value2);
            string id = value;
            string pass = value2;
            tf = hashTable.verify(id, pass);
            if (tf == true)
            {
                cout << "That is the correct password." << endl;
            }
            else
            {
                cout << "That is not the correct password." << endl;
            }
            continue;
        }

        // HOME /////////////////////////////////////////////////////////////////////////////////////////

        else if (command == "home")
        {
            getWord(ss, value);
            getWord(ss, value2);
            string id = value;
            string directory = value2;
            tf = hashTable.setDirectory(id, directory);
            if (tf == true)
            {
                cout << "Directory successfully changed." << endl;
            }
            else
            {
                cout << "Failed to change directory. Please try again." << endl;
            }
            continue;
        }

        // PASSWD //////////////////////////////////////////////////////////////////////////////////////

        else if (command == "passwd")
        {
            getWord(ss, value);
            getWord(ss, value2);
            string id = value;
            string pass = value2;
            tf = hashTable.setPassword(id, pass);
            if (tf == true)
            {
                cout << "Password successfully changed." << endl;
            }
            else
            {
                cout << "Failed to change password. Please try again." << endl;
            }
            continue;
        }

        cout << "Error! Unexpected command entered." << endl;
    }
    return true;
}

int main()
{
    parseStream(cin);
}