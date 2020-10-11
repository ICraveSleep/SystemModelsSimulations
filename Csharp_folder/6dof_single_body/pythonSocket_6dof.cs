using System.Collections;
using System.Collections.Generic;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using UnityEngine;

public class pythonSocket : MonoBehaviour
{

    //public Rigidbody rigidbody;

    Thread mThread;

    public string connectionIP = "127.0.0.1";
    public int connectionPort = 25001;

    IPAddress localAddress;

    TcpListener pythonListener;
    TcpClient pythonClient;

    Vector3 receivedTransformRotation = Vector3.zero;
    Vector3 receivedTransformPosition = Vector3.zero;
    Quaternion rotate;

    bool running;

    void SendAndReceiveData()
    {
        NetworkStream natworkStream = pythonClient.GetStream();
        byte[] buffer = new byte[pythonClient.ReceiveBufferSize];

        // Receiving Data from the Host (Python side)
        int bytesRead = natworkStream.Read(buffer, 0, pythonClient.ReceiveBufferSize); //Getting data in Bytes from Python
        string dataReceived = Encoding.UTF8.GetString(buffer, 0, bytesRead); //Converting byte data to string

        if (dataReceived != null)
        {
            //---Using received data---
            receivedTransformPosition = StringToVector3(dataReceived); //<-- assigning receivedPos value from Python
            receivedTransformRotation = StringToVector3Rotation(dataReceived); //<-- assigning receivedPos value from Python
            print("received pos data, and moved the Cube!");

            //---Sending Data to Host----
            byte[] myWriteBuffer = Encoding.ASCII.GetBytes("Hey I got your message Python! Do You see this massage?"); //Converting string to byte data
            natworkStream.Write(myWriteBuffer, 0, myWriteBuffer.Length); //Sending the data in Bytes to Python
        }

    }
    void GetInfo()
    {
        localAddress = IPAddress.Parse(connectionIP);
        pythonListener = new TcpListener(IPAddress.Any, connectionPort);
        pythonListener.Start();

        pythonClient = pythonListener.AcceptTcpClient();

        running = true;
        while (running)
        {
            SendAndReceiveData();
        }
        pythonListener.Stop();
    }
    // Start is called before the first frame update
    private void Start()
    {
        ThreadStart TCPthread = new ThreadStart(GetInfo);
        mThread = new Thread(TCPthread);
        mThread.Start();

    }

    // Update is called once per frame
    void Update()
    {
        rotate = Quaternion.Euler(receivedTransformRotation);
        transform.rotation = rotate; //assigning receivedPos in SendAndReceiveData()
        transform.position = receivedTransformPosition;
    }


    public static Vector3 StringToVector3(string sVector)
    {
        // Remove the parentheses
        if (sVector.StartsWith("(") && sVector.EndsWith(")"))
        {
            sVector = sVector.Substring(1, sVector.Length - 2);
        }

        // split the items
        string[] sArray = sVector.Split(',');

        Debug.Log(sArray);

        // store as a Vector3
        Vector3 result = new Vector3(
            float.Parse(sArray[0]),
            float.Parse(sArray[1]),
            float.Parse(sArray[2]));

        return result;
    }

    public static Vector3 StringToVector3Rotation(string sVector)
    {
        // Remove the parentheses
        if (sVector.StartsWith("(") && sVector.EndsWith(")"))
        {
            sVector = sVector.Substring(1, sVector.Length - 2);
        }

        // split the items
        string[] sArray = sVector.Split(',');

        Debug.Log(sArray);

        // store as a Vector3
        Vector3 result = new Vector3(
            float.Parse(sArray[3]),
            float.Parse(sArray[4]),
            float.Parse(sArray[5]));

        return result;
    }

    /*
    public static string GetLocalIPAddress()
    {
        var host = Dns.GetHostEntry(Dns.GetHostName());
        foreach (var ip in host.AddressList)
        {
            if (ip.AddressFamily == AddressFamily.InterNetwork)
            {
                return ip.ToString();
            }
        }
        throw new System.Exception("No network adapters with an IPv4 address in the system!");
    }
    */

}
