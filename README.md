# Smart Device Management System

## Introduction
The Smart Device Management System is a Python-based software application designed to manage a network of smart home devices. It provides a centralized interface to monitor and control various devices, each with common foundational traits as well as unique, specialized capabilities.

## Task Summary
This project demonstrates core Object-Oriented Programming (OOP) principles in Python. The system architecture includes:
* **Classes and Objects:** A parent `SmartDevice` class establishes the baseline framework, while specialized child classes (`TemperatureSensor`, `SecurityCamera`, and `SmartLight`) introduce unique attributes and methods.
* **Inheritance:** Child classes successfully inherit common attributes (like name, device ID, and power status) and utilize `super()` for efficient initialization.
* **Encapsulation:** Sensitive system information is protected. Attributes such as the `device_id` and `brightness` are shielded from direct, unvalidated modification using Python `@property` decorators and setter methods to maintain system integrity.
* **Interactive Interface:** A while-loop-driven terminal menu allows users to continuously interact with the instantiated objects, turn devices on/off, read sensors, and adjust specific device settings.

## How to Run the Program
1. Ensure you have Python installed on your machine.
2. Clone this repository to your local system.
3. Open your terminal or command prompt and navigate to the project directory.
4. Execute the Python script by running:
   ```bash
   python Mini_Projects.py
   ```
5. Follow the on-screen prompts to navigate the menu using your keyboard (typing numbers 1 through 7). The system includes slight wait times for a smoother terminal reading experience.

## Author
* **Name:** Essel
* **Institution:** University of Mines and Technology (UMaT)
* **Location:** Tarkwa
* **Course:** EL 162 / 234 Object Oriented Programming
