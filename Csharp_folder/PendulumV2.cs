using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PendulumV2 : MonoBehaviour
{

    public Rigidbody rigidbody;

    public float L = 2.0f;             /*Lenght of the rope*/
    public float g = 9.81f;             /*Gravity force*/


    public float theta0 = 1 * Mathf.PI;/*Initial angle. Must be different from 0*/
    public float omega0 = 0;                /*Initial angular velocity*/
    public float tdd0 = 0;


    public float theta_k;                /*Theta value in step K*/
    public float omega_k;                /*Omega value in step K*/
    public float tdd_k;
    public float omega_k1;               /*Omega value in step K+1*/
    public float theta_k1;               /*Theta value in step K+1*/
    public float tdd_k1;
    //    public Vector3 p, p0;
    //    Vector3 v;

    Quaternion rotate;
    void Awake()
    {
        omega_k = omega0;
        theta_k = theta0;
    }

    void FixedUpdate()
    {
        tdd_k = -g / L * Mathf.Sin(theta_k) + tdd0;

        omega_k1 = omega_k + tdd_k * Time.deltaTime;
        omega_k = omega_k1;

        theta_k1 = theta_k + omega_k1 * Time.deltaTime;
        theta_k = theta_k1;
        //transform.rotation.y = theta_k1;
        rotate = Quaternion.Euler(theta_k1*180/Mathf.PI, 0, 0);
        rigidbody.MoveRotation(rotate);
        //Vector3 rtation = [rotate, 0, 0];
        //transform.rotation.eulerAngles.x = rotate;
    }
}
