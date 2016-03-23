#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/20 23:16

def population():
    populationBorn = 1/7.0
    populationDie = 1/13.0
    populationAdd = 1/45
    populationSecond = populationBorn + populationAdd - populationDie
    # currentPopulation = 3120324986
    oneYearToSecond = 365 * 24 * 3600
    perYearAddPopulation =  oneYearToSecond * populationSecond
    return  perYearAddPopulation
if __name__ == "__main__":
    currentPopulation = 3120324986
    print("first year population",int(population() + currentPopulation))
