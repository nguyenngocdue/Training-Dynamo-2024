using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Autodesk.DesignScript.Runtime;

namespace dynBIM3DM.Math
{
    //[IsVisibleInDynamoLibrary(false)]
    public static class Operations
    {
        public static double Add(double a, double b)
        {
            return a + b;
        }

        public static double Multiply(double a, double b)
        {
            return a * b;
        }
    }
}

namespace MyCustomNodes.Utils
{
    public static class Logger
    {
        public static void Log(string message)
        {
            Console.WriteLine(message);
        }
    }
}
