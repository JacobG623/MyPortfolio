#pragma once
#include <string>
#include <vector>
#include <list>
#include "User.h"

using std::string;
using std::vector;
using std::list;

// Hash class based on example from Geeksforgeeks
class hash
{
private:
	user** table;
	int capacity;
	user* deleted;
	int size;

public:
	hash(int capacity);
	void insertItem(string id, string directory, string pass);
	void display();
	void clear();
	void resizeTable();
	void saveTable(string file);
	void loadTable(string file);
	bool userDisplay(string id);
	bool deleteItem(string id);
	bool verify(string id, string pass);
	bool setDirectory(string id, string directory);
	bool setPassword(string id, string pass);
	int hashFunction(string id);
};