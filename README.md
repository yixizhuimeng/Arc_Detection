# Arc_Detection
Sunspark

Because of the size of the data, the data warehouse is given as a link：
Link：https://pan.baidu.com/s/1OgOAw-IvqSDnZd76dC4JuQ 
Code：hbhl

About Dataset:
The Arc Fault Detection Database is acquired by the arc fault collector based on electromagnetic induction under the voltage of 100-300V. Due to the non-obvious arc fault status of some data under certain scenarios and voltages, we uniformly filtered this part of the data. In the database, we use 0 to represent the collected normal current and 1 to represent the arc fault current in different situations.
The relevant directories for the dataset are as follows：
'''│  list.txt
│
├─test
│  │  test.txt
│  │  
│  ├─capacitance1uf
│  ├─inductance80uh
│  │  └─150V
│  │      ├─0
│  │      └─1
│  └─seven_group_resistors4
│      ├─150V
│      │  ├─0
│      │  └─1
│      ├─200V
│      │  ├─0
│      │  └─1
│      ├─250V
│      └─300V
└─train
    │  train.txt
    │  
    ├─capacitance1uf
    │  └─200V
    │      ├─0
    │      └─1
    ├─inductance80uh
    │  └─150V
    │      ├─0
    │      └─1
    └─seven_group_resistors4
        ├─150V
        │  ├─0
        │  └─1
        ├─200V
        │  ├─0
        │  └─1
        ├─250V
        │  ├─0
        │  └─1
        └─300V
            ├─0
            └─1
'''
'''
├─test
│  ├─capacitance1uf
│  ├─inductance80uh
│  │  └─150V
│  │      ├─0
│  │      └─1
│  └─seven_group_resistors4
│      ├─150V
│      │  ├─0
│      │  └─1
│      ├─200V
│      │  ├─0
│      │  └─1
│      ├─250V
│      └─300V
└─train
    ├─capacitance1uf
    │  └─200V
    │      ├─0
    │      └─1
    ├─inductance80uh
    │  └─150V
    │      ├─0
    │      └─1
    └─seven_group_resistors4
        ├─150V
        │  ├─0
        │  └─1
        ├─200V
        │  ├─0
        │  └─1
        ├─250V
        │  ├─0
        │  └─1
        └─300V
            ├─0
            └─1
            '''
