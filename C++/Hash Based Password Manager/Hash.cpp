#include "Hash.h"
#include <iostream>
#include<fstream>

using std::cout;
using std::endl;
using std::ifstream;
using std::ofstream;

hash::hash(int value)
{
	capacity = value;
	table = new user*[capacity];
	size = 0;
	for (int i = 0; i < capacity; i++)
	{
		table[i] = NULL;
	}
	deleted = new user("-1", "-1", "-1");
}

int hash::hashFunction(string id)
{
	int key = 0;
	for (int i = 0; i < id.size(); i++)
	{
		key += int(id[i]);
	}
	return (key % capacity);
}

void hash::insertItem(string id, string directory, string pass)
{
	user* temp = new user(id, directory, pass);
	int index = hashFunction(id);
	int i = 0;
	while (table[index] != NULL && table[index]->userID != id && table[index]->userID != "-1")
	{
		index = index + i ^ 2;
		index = index % capacity;
		i++;
	}
	if (table[index] == NULL || table[index]->userID == "-1")
	{
		size++;
	}
	table[index] = temp;
	if (size > (capacity / 2))
	{
		resizeTable();
	}
}

bool hash::deleteItem(string id)
{
	int index = hashFunction(id);
	int i = 0;
	while (table[index] != NULL)
	{
		if (table[index]->userID == id)
		{
			table[index] = deleted;
			size--;
			return true;
		}
		index = index + i ^ 2;
		index = index % capacity;
		i++;
	}
	return false;
}

void hash::display()
{
	for (int i = 0; i < capacity; i++)
	{
		if (table[i] != NULL && table[i]->userID != "-1")
		{
			cout << "userID: " << table[i]->userID << "  Password: " << table[i]->password << "  Home Directory: " << table[i]->homeDirectory << endl;
		}
		else if (table[i] != NULL && table[i]->userID == "-1")
		{
			cout << "userID: deleted  Password: deleted  Home Directory: deleted" << endl;
		}
		else
		{
			cout << "userID: --  Password: --  Home Directory: --" << endl;
		}
	}
}

bool hash::userDisplay(string id)
{
	int index = hashFunction(id);
	int i = 0;
	while (table[index] != NULL)
	{
		if (table[index]->userID == id)
		{
			cout << "userID: " << table[index]->userID << "  Password: " << table[index]->password << "  Home Directory: " << table[index]->homeDirectory << endl;
			return true;
		}
		index = index + i ^ 2;
		index = index % capacity;
		i++;
	}
	return false;
}

void hash::clear()
{
	capacity = 23;
	size = 0;
	for (int i = 0; i < capacity; i++)
	{
		table[i] = NULL;
	}
}

bool hash::verify(string id, string pass)
{
	int index = hashFunction(id);
	int i = 0;
	while (table[index] != NULL)
	{
		if (table[index]->userID == id)
		{
			if (table[index]->password == pass)
			{
				return true;
			}
		}
		index = index + i ^ 2;
		index = index % capacity;
		i++;
	}
	return false;
}

bool hash::setDirectory(string id, string directory)
{
	int index = hashFunction(id);
	int i = 0;
	while (table[index] != NULL)
	{
		if (table[index]->userID == id)
		{
			table[index]->homeDirectory = directory;
			return true;
		}
		index = index + i ^ 2;
		index = index % capacity;
		i++;
	}
	return false;
}

bool hash::setPassword(string id, string pass)
{
	int index = hashFunction(id);
	int i = 0;
	while (table[index] != NULL)
	{
		if (table[index]->userID == id)
		{
			table[index]->password = pass;
			return true;
		}
		index = index + i ^ 2;
		index = index % capacity;
		i++;
	}
	return false;
}

void hash::resizeTable()
{
	ifstream is;
	is.open("prime.txt");
	string value;
	int value2 = 0;
	while (getline(is, value) && value2 < capacity * 2)
	{
		value2 = stoi(value);
	}
	user** temp = new user * [capacity];
	for (int i = 0; i < capacity; i++)
	{
		temp[i] = table[i];
	}
	hash table(value2);
	for (int i = 0; i < capacity; i++)
	{
		if (temp[i]->userID != "")
		{
			table.insertItem(temp[i]->userID, temp[i]->homeDirectory, temp[i]->password);
		}
	}
}

void hash::saveTable(string file)
{
	ofstream os;
	os.open(file);
	string data;
	for (int i = 0; i < capacity; i++)
	{
		if (table[i] != NULL && table[i]->userID != "-1")
		{
			data = "userID: " + table[i]->userID + "  Password: " + table[i]->password + "  Home Directory: " + table[i]->homeDirectory;
		}
		os << data << endl;
	}
	os.close();
}

void hash::loadTable(string file)
{
	ifstream is;
	is.open(file);
	string id;
	string directory;
	string pass;
	while (true)
	{
		getline(is, id, ' ');
		if (id != "")
		{
			getline(is, directory, ' ');
			getline(is, pass, ' ');
			insertItem(id, directory, pass);
		}
		else
		{
			break;
		}
	}
}