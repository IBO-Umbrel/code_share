using Types;
using Tashkent.Novza;
using Tashkent.Novza.MUUniversity;


namespace Tashkent
{
    namespace Novza
    {
        namespace MUUniversity
        {
            class Student(string first_name, string last_name, string group)
            {
                public string FirstName { get; } = first_name;
                public string LastName { get; } = last_name;
                public string Group { get; set; } = group;
            }
            class Professor(string first_name, string last_name, string profession)
            {
                public string FirstName { get; } = first_name;
                public string LastName { get; } = last_name;
                public string Profession { get; } = profession;
            }
        }
        class Station
        {
            public DateTime TrainArival = new DateTime();
        }
    }
}
namespace Types
{
    class Sorter(List<object> list)
    {
        public List<bool> Booleans { get; } = list.OfType<bool>().ToList();
        public List<string> Strings { get; } = list.OfType<string>().ToList();
        public List<int> Ints { get; } = list.OfType<int>().ToList();
    }
}
namespace csharp
{
    class Program
    {
        static void Main()
        {
            // List<object> ob_list = ["good", true, 10, false, true, "googling", 3.3];

            // object[] ob_array = ["good", true, 10, false, true, "googling", 3.3];


            // Sorter sorted = new Sorter(ob_list);
            // sorted.Ints.ForEach(x => Console.WriteLine(x));

            // Station station = new Station();
            // Console.WriteLine(station.TrainArival);

            Student student_1 = new Student("ibrohimjon", "toshtemirov", "IT-102");
            Student student_2 = new Student("abdurohmon", "unknown", "IT-101");
            Student student_3 = new Student("azizbek", "unknown", "BM-103");

            List<Student> students = [student_1, student_2, student_3];

            students.ForEach(x => Console.WriteLine(x.FirstName + " " + x.LastName + " " + x.Group + "\n"));
        }
    }
}