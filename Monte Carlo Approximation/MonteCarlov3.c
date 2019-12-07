/*  Monte-Carlo Integration Approximation C version 3
    Copyright (C) 2019 Matthew Hoffman (https://github.com/nordkamp/)
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

double eq1(double x) {
    return sqrt(25-pow(x,2));
}

int pointgen(double limits[], int points) {
    int count, pointcount = 0;
    double x, y;
    srand(time(NULL));
    for (count = 0; count != points; count++) {
        if (limits[2] + (rand() / (RAND_MAX/(limits[3]-limits[2]))) < eq1(limits[0] + (rand() / (RAND_MAX/(limits[1]-limits[0]))))) {
            pointcount++;
        }
    }
    return pointcount;
}

int main() {
    int points, insideof;
    double area, limits[4], areaest;
    printf("Enter number of random points: ");
    scanf("%d",&points);
    printf("Enter the lower x bound: ");
    scanf("%lf",&limits[0]);
    printf("Enter the upper x bound: ");
    scanf("%lf",&limits[1]);
    printf("Enter the lower y bound: ");
    scanf("%lf",&limits[2]);
    printf("Enter the upper y bound: ");
    scanf("%lf",&limits[3]);
    area = (abs(limits[0])+abs(limits[1]))*(abs(limits[2])+abs(limits[3]));
    insideof = pointgen(limits, points);
    areaest = insideof*area/points;
    printf("Points inside the curve: %d\nThe area estimate is: %lf\n",insideof,areaest);
    

}