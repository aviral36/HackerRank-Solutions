class Person {
public:
    string name;
    int age;
    virtual void getdata() {
        cin >> name >> age;
    }
    virtual void putdata() {
        cout << name << " " << age << endl;
    }
};

class Professor : public Person {
public:
    Professor() {
        cur_id = ++id;
    }
    int publications;
    static int id;
    int cur_id;
    void getdata() {
        cin >> name >> age >> publications;
    }
    void putdata() {
        cout << name << " "
            << age << " "
            << publications << " "
            << cur_id << endl;
    }
};
int Professor::id = 0;

class Student : public Person {
#define NUM_OF_MARKS 6
public:
    Student() {
        cur_id = ++id;
    }
    int marks[NUM_OF_MARKS];
    static int id;
    int cur_id;
    void getdata() {
        cin >> name >> age;
        for (int i=0; i<NUM_OF_MARKS; i++) {
            cin >> marks[i];
        }
    }
    void putdata() {
        int marksSum = 0;
        for (int i=0; i<NUM_OF_MARKS; i++) {
            marksSum += marks[i];
        }
        cout << name << " "
            << age << " "
            << marksSum << " "
            << cur_id << endl;
    }
};
int Student::id = 0;
