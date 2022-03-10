namespace Shutdowner
{
    using System.Diagnostics;
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hejjo");
            Process cmd = new Process();
            cmd.StartInfo.FileName = "cmd.exe";
            // Delay shutdown with 20 seconds to enable user to cancel with 'shutdown -a' in separate cmd.
            cmd.StartInfo.Arguments = "/c shutdown /s /t 20";
            cmd.StartInfo.CreateNoWindow = true;
            cmd.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
            cmd.Start();
        }
    }
}