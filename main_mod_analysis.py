#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Heart Attack Analysis
Main Module for running analysis
"""

import utilities_analysis as ut


def main():
     
    # Display app header informative information
    print("\nHeart Attack Analysis")
    print("\nThese are the factors related to heart attacks that are considered in this data:")
    print("\t1. Heart Attack Percentage is calculated based on all data to see if the data is skewed.")
    print("\t2. Gender Percent is used to distinguish between the heart attack rates in men and women.")

    print("\t5. EKG is considered, as it detects heart problems that can forecast chance of future heart attacks.")
    print("\t6. Exercise is considered to see if likelihood of heart attack increases when physically active.")  
    
    # Perform Heart Attack Percents
    ut.getHeart()
  
    # Perform Gender Percents
    ut.getGender()

 
    # Perform EKG Analysis
    ut.getEKG()

    # Perform Exercise Analysis
    ut.getExercise()    
  
#---------------------------Code Entry Point---------------------------#
if __name__ == "__main__":
    main()