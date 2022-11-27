#include<iostream>
#include<stack>
#include<string>
#include<cstring>
using namespace std;
 
class Exp
{
    stack<char> ops;
    stack<char> ds; 
    double v,lh,rh; 
    char op;   
    public:
        double calinput() 
        {
            do
            {
                readdata();  
                skipspace();  
            }while(readop());  
 
            calremain();
            return v;
        }
 
        void readdata()  
        {
            while(!(cin >> v))  
            {
                cin.clear();
                cin >> op;    
                if(op != '(')
                {
                    throw string("need a number but find ") + op;
                }
                ops.push(op);
            }
            ds.push(v);
        }
 
        void skipspace()  
        {
            while(cin.peek() == ' ' || cin.peek() == '\t')
            {
                cin.ignore();
            }
        }
 
        bool readop()  
        {
            while((op=cin.get()) == ')')
            {
                while(ops.top() != '(') 
                {
                    rh = ds.top(); ds.pop(); 
                    lh = ds.top(); ds.pop(); 
                    ds.push(cal(lh,ops.top(),rh));
                    ops.pop();
                }
                ops.pop();  
            }
 
            if(op == '\n') return false;
            if(strchr("+-*/",op) == NULL)
            {
                throw string("invalid operator")+op;
            }
 
            while(!ops.empty() && ops.top() != '(' && prior(op,ops.top()))
            {
                rh = ds.top(); ds.pop(); 
                lh = ds.top(); ds.pop();
                ds.push(cal(lh,ops.top(),rh)); 
                ops.pop();
            }
            ops.push(op);  
            return true;
        }
 
        void calremain()
        {
            while(!ops.empty())
            {
                rh = ds.top(); ds.pop(); 
                lh = ds.top(); ds.pop(); 
                ds.push(cal(lh,ops.top(),rh)); 
                ops.pop();
            }
            if(ds.size()!= 1) 
            {
                throw string("invalid expression");
            }
            v = ds.top();
            ds.pop();
        }
 
        double cal(double lh, char op, double rh)
        {
            return op == '+' ? lh + rh :
                   op == '-' ? lh - rh :
                   op == '*' ? lh * rh : lh/rh;
                    
        }
 
        bool prior(char op1, char op2)  
        {
            return op1 != '+' && op1 != '-' && op2 != '*' && op2 != '/';
        }
};
 
int main()
{
    Exp e;
    try
    {
        cout << e.calinput() <<endl;
    }
    catch(const string& e)
    {
        cout << e <<endl;
    }
    
}