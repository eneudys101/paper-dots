#include <stdio.h>

typedef struct{
    int id, arrival_time, duration;
}Rider;

void fcfs(Rider riders[], int rider_amount){
    
    int current_time = 0;
    int ride_time = 3;
    int current_rider = 0;
    
    //goes through all the riders in the queue
    //for(int rider = 0; rider < length, rider++){ 
    while(current_rider < rider_amount ){    
        
        current_rider = 0;
        for(int ride_timer = 0; ride_timer < ride_time; ride_timer++){          
            current_time++;
            
            printf("Current rider arrival time: %d", riders[current_rider].arrival_time);
            if(riders[current_rider].arrival_time > current_time && current_time % ride_timer == 0){
                riders[current_rider].duration++; 
            }

        }
        current_rider++;
    }
}


int main(){
    int total = 3;
    Rider rider_array[] ={ {1, 2, 0} , {2, 5, 0}, {3, 7, 0} };
    fcfs(rider_array,total);

    for(int i = 0; i < total; i++){
        printf("Rider %d: - Duration %d: ",rider_array[i].id, rider_array[i].duration);
    }
    return 0;
}
