#pragma once
#include <string>

using std::string;

class user
{
public:
	string userID;
	string homeDirectory;
	string password;
	user() : userID(""), homeDirectory(""), password("") {}
	user(string id, string directory, string pass) : userID(id), homeDirectory(directory), password(pass) {}
};