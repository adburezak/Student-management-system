#include <iostream>

using namespace std;

// Node structure
struct Node {
  int id;
  string name;
  string course;
  Node* prev;
  Node* next;
};

// Head and tail pointers
Node* head = NULL;
Node* tail = NULL;

// Function to add a student at the beginning
void add_at_beginning(int id, string name, string course) {
  // Create new node
  Node* new_node = new Node;
  new_node->id = id;
  new_node->name = name;
  new_node->course = course;

  // Update pointers
  if (head ==NULL) {
    head = new_node;
    tail = new_node;
    new_node->prev =NULL ;
    new_node->next = NULL;
  } else {
    new_node->next = head;
    head->prev = new_node;
    head = new_node;
    new_node->prev = NULL;
  }
}

// Function to add a student at the end
void add_at_ending(int id, string name, string course) {
  // Create new node
  Node* new_node = new Node;
  new_node->id = id;
  new_node->name = name;
  new_node->course = course;

  // Update pointers
  if (tail ==NULL) {
    head = new_node;
    tail = new_node;
    new_node->prev = NULL;
    new_node->next = NULL;
  } else {
    tail->next = new_node;
    new_node->prev = tail;
    tail = new_node;
    new_node->next =NULL;
  }
}

// Function to display student records forward
void forward_display() {
  Node* current = head;
  if (current == NULL) {
    cout << "List is empty!" << endl;
    return;
  }

  cout << "Student Records:" << endl;
  while (current != NULL) {
    cout << "ID: " << current->id << ", Name: " << current->name << ", Course: " << current->course << endl;
    current = current->next;
  }
}

// Function to display student records backward
void backward_display() {
  Node* current = tail;
  if (current == NULL) {
    cout << "List is empty!" << endl;
    return;
  }

  cout << "Student Records (backward):" << endl;
  while (current !=NULL) {
    cout << "ID: " << current->id << ", Name: " << current->name << ", Course: " << current->course << endl;
    current = current->prev;
  }
}

// Function to delete a student from the beginning
void delete_from_beginning() {
  if (head == NULL) {
    cout << "List is empty!" << endl;
    return;
  }

  // Update pointers
  Node* temp = head;
  head = head->next;
  if (head != NULL) {
    head->prev = NULL;
  } else {
    tail = NULL;
  }

  delete temp;
  cout << "Student deleted from the beginning!" << endl;
}

// Function to delete a student from the ending
void delete_from_ending() {
  if (tail == NULL) {
    cout << "List is empty!" << endl;
    return;
  }

  // Update pointers
  Node* temp = tail;
  tail = tail->prev;
  if (tail != NULL) {
    tail->next = NULL;
  } else {
    head = NULL;
  }

  delete temp;
  cout << "Student deleted from the ending!" << endl;
}

int main() {
  int choice, id;
  string name, course;

  while (true) {
           cout<<"----------Haramaya University---------"<<endl;
        cout<<"------------College of Computing and Informatics-----------"<<endl;
        cout<<"--------Department of Information Technology-------"<<endl;
    cout << "-----Student Registration System using  Double Linked List -----" << endl;
    cout<<"======= lakewu siyum 3259/14 ======"<<endl;
    cout<<"======= mohammed asfaw t/4919/14 ======="<<endl;
    cout<<"======= kedir mustefa 3226/14 ========"<<endl;
    cout<<"====== samual terfa 1489/14 ========"<<endl;
    cout<<"====== messaye yewala 3428/14 ========"<<endl;
    cout << "1. Add student at beginning" << endl;
    cout << "2. Add student at ending" << endl;
    cout << "3. Delete student from beginning" << endl;
    cout << "4. Delete student from ending" << endl;
    cout << "5. Display student records forward" << endl;
    cout << "6. Display student records backward" << endl;
    cout << "7. Exit" << endl;
    cout << "Enter your choice: ";
    cin >> choice;

    switch (choice) {
      case 1:
        // Add student at beginning
        cout << "Enter ID, name, and course: ";
        cin >> id >> name >> course;
        add_at_beginning(id, name, course);
        break;

      case 2:
        // Add student at ending
        cout << "Enter ID, name, and course: ";
        cin >> id >> name >> course;
        add_at_ending(id, name, course);
        break;

      case 3:
        // Delete student from beginning
        cout << "Enter ID, name, and course: ";
        cin >> id >> name >> course;
        delete_from_beginning();
        break;

      case 4:
        // Delete student from ending
        cout << "Enter ID, name, and course: ";
        cin >> id >> name >> course;
        delete_from_ending();
        break;

      case 5:
        // Display student records forward
        cout << "Enter ID, name, and course: ";
        cin >> id >> name >> course;
        forward_display();
        break;

      case 6:
        // Display student records backward
        cout << "Enter ID, name, and course: ";
        cin >> id >> name >> course;
        backward_display();
        break;

      case 7:
        // Exit program
        return(0);

      default:
        cout << "Invalid choice! Please try again." << endl;
    }
  }

  return 0;
}

