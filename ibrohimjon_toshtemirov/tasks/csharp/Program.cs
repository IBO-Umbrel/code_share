// C# tasks: using for loop


// 1️⃣ Print numbers from 50 to 100.
for (int i = 50; i <= 100; i++)
{
    Console.WriteLine(i);
}


// 2️⃣ Print all multiples of 3 between 1 and 30.
for (int i = 1; i <= 30; i++)
{
    if (i % 3 == 0)
    {
        Console.WriteLine(i);
    }
}


// 3️⃣ Print a sequence: 5, 10, 15, 20, ..., 50.
for (int i = 5; i <= 50; i += 5)
{
    Console.WriteLine(i);
}


// 4️⃣ Count and print how many even numbers are in a given range (1 to 50).
int count = 0;
for (int i = 1; i <= 50; i++)
{
    if (i % 2 == 0)
    {
        count++;
    }
}
Console.WriteLine(count);


// 5️⃣ Print the sum of the first 20 natural numbers.
int sum = 0;
for (int i = 1; i <= 20; i++)
{
    sum += i;
}
Console.WriteLine(sum);


// 6️⃣ Print the reverse of a given number (e.g., 123 → 321).
int number = 123;
string numberStr = number.ToString();
for (int i = numberStr.Length - 1; i >= 0; i--)
{
    Console.Write(numberStr[i]);
}
Console.WriteLine();


// 7️⃣ Print the ASCII values of characters from 'A' to 'Z'.
for (char c = 'A'; c <= 'Z'; c++)
{
    Console.WriteLine((int)c);
}


// 9️⃣ Check if a number is prime using a for loop.
int num = 100;
bool isPrime = true;
for (int i = 2; i <= num / 2; i++)
{
    if (num % i == 0)
    {
        isPrime = false;
        break;
    }
}
Console.WriteLine(isPrime ? "Prime" : "Not Prime");


// 🔟 Print a pyramid of numbers (up to 5 rows).
for (int i = 1; i <= 5; i++)
{
    for (int j = 1; j <= i; j++)
    {
        Console.Write(i);
        Console.Write(j);
    }
    Console.WriteLine();
}