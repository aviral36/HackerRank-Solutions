
//l,b,h are integers representing the dimensions of the box

// Constructors: 
// Box();
// Box(int,int,int);
// Box(Box);

class Box{
    int l, b, h;
    public:
    Box(){
        l=0;
        b=0;
        h=0;
    }
    Box(int x, int y, int z){
        l=x;
        b=y;
        h=z;
    }
    Box(const Box &B){
        l = B.l;
        b = B.b;
        h = B.h;
    }
    int getLength(){    
        return l;       // Return box's length
    }
    int getBreadth(){
        return b;       // Return box's breadth
    }
    int getHeight(){
        return h;        // Return box's height
    }
    long long CalculateVolume(){
        long long V = l*b;  // Return the volume of the box
        V = V*h;
        return V;
    }
    bool operator<(Box B){
        int flag = 0;
        if(l<B.l)
            flag += 1;
        if(b<B.b && l==B.l)
            flag += 1;
        if(h<B.h && l==B.l && b==B.b)
            flag += 1;
        if(flag>0)
            return true;
        else return false;
    }
    friend ostream & operator<<(ostream & out, Box & B);
};

ostream & operator<<(ostream & out, Box & B){
        out<<B.l<<" "<<B.b<<" "<<B.h;
        return out;
}


//Overload operator < as specified
//bool operator<(Box& b)

//Overload operator << as specified
//ostream& operator<<(ostream& out, Box& B)
