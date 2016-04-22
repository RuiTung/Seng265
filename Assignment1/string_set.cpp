/**
 * For Assignment 1 : V00800795 Rui Ma, October 2nd, 2015 
 * String_set.cpp
 */


#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "string_set.h"

using namespace std;

//initialize hash_table, iterator_index and iterator_node
string_set::string_set() {

    *hash_table = new node[HASH_TABLE_SIZE];
    iterator_index = 0;
    iterator_node = NULL;
    for (int i = 0; i < HASH_TABLE_SIZE; i++) {
       hash_table[i] = NULL;
    }
}

/**
* if s exist, throw duplicate_exception
* otherwise, allocate space for a new node and for s.
* insert the new node at the front of the list headed
* by hash_table[i], where i is hash_function(s)
*/
void string_set::add(const char *s) {

	int ascii = hash_function(s);
	node* newNode = new node();
	newNode -> s = (char *)s;
    newNode -> next = NULL;

    // when empty, start a new list
    if(hash_table[ascii % 100] == 0) {
        hash_table[ascii % 100] = newNode;
        return;
    }


    node *next = hash_table[ascii % 100];
    node *current = next;
    // when the position exist node then put it to the end of the node list
    while(next) {
        current = next;
        string s1(current -> s);
        string s2(s);
        if(s1.compare(s2) == 0) {
            throw duplicate_exception();
        }
        next = current -> next;
    }
    current -> next = newNode;
}

/**
* if s is not exist, throw not_found_exception
* otherwise, remove the node containing s
*/
void string_set::remove(const char *s) {

	int ascii = hash_function(s);
    node *found = hash_table[ascii % 100];
    node *current = found;
    node *pre = found;
    if(!found) {
        throw not_found_exception();
    }

    while(current) {
        string s1(current -> s);
        string s2(s);
        if(s1.compare(s2) == 0) {
          // remove the node and reconnect previous with next node
          if(current == found) {
             hash_table[ascii % 100] = found -> next;
          }
          else {
             pre -> next = current -> next;
          }
          iterator_index = 0;
          return;
        }
        pre = current;
        current = current -> next;
    }
    //fail to find the same string after scan the node list
    throw not_found_exception();
}

//if s exist, return 1; otherwise return 0
int string_set::contains(const char *s) {

	int ascii = hash_function(s);
    node *found = hash_table[ascii % 100];
    node *current = found;
    if(!found) {
       return 0;
    }

    // loop node list to see if there is any node match the string
    while(current) {
        string s1(current -> s);
        string s2(s);
        if(s1.compare(s2) == 0) {
          current = NULL;
          iterator_index = 0;
          return 1;
        }
        current = current -> next;
    }
    //fail to find the same string after scan the node list
    return 0;
}

//reset the iterator to the first element
void string_set::reset() {

	iterator_index = 0;
    iterator_node = NULL;
}

//return the next avaliable string or NULL if no more elements remain
const char *string_set::next() {

    // iterator_index == -1 means scanned to the end
    if(iterator_index == -1) {
       iterator_node = NULL;
       return NULL;
    }

    for (int i = iterator_index; i < HASH_TABLE_SIZE; i++) {
        if(hash_table[i]) {
            // first time next() is invoked
            if(iterator_node == 0) {
                node* current = hash_table[i];
                while(current -> next != 0) {
                    current = current -> next;
                }
                iterator_node = current;
                iterator_index = i;
                break;
            }
            else if(iterator_node == hash_table[i]) {
                // deal with head node, if last node is head node,
                // move on to the next row
                iterator_node = NULL;
                continue;
             }
            // deal with none-head-node 
            else {
                node* current = hash_table[i];
                while(current -> next != iterator_node) {
                    current = current -> next;
                }
                iterator_index = i;
                iterator_node = current;
                break;
            }
        }
        iterator_node = NULL;
        iterator_index = -1;
    }
	return iterator_node == 0 ? NULL : iterator_node -> s;
}

//delete all dynamic storage allocated for nodes and strings
string_set::~string_set() {
    for (int i = 0; i < HASH_TABLE_SIZE; i++ ) {
       delete hash_table[i];
    }
}

//map a string to an integer between 0 and HASH_TABLE-SIZE-1.
int string_set::hash_function(const char *s) {
    int hash = 0;
    for(char* ch = (char*)s; *ch; ++ch) {
        hash += (int)(*ch);
    }
	return hash % 100;
}
