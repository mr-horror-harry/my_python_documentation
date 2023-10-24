import math as mt 

print(mt.floor(3.352)) #next immediate whole no.
print(mt.ceil(3.352)) #previous immediate whole no.

print(round(4.34535)) #rounding off

print("Exponential:",mt.e,
        " Infinfity:", mt.inf,
            " Nan:", mt.nan
)

#logarithmic
print(mt.log(2)) #base to exp
print(mt.log(100, 10)) #base to 10 => 2
#means 10**2 => 100
print(mt.log(mt.e))

#trignometry
print(mt.sin(mt.radians(90))) # to degree