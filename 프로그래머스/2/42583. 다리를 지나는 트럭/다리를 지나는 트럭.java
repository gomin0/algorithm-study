import java.util.*;
class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<Integer> q = new LinkedList<>();
        int sum = 0;        
        int answer = 0;
        
        if (bridge_length == 1) {
            return truck_weights.length;
        }
        if (truck_weights.length == 1) {
            return bridge_length + 1;
        }
        
        for(int i = 0; i < truck_weights.length; i++) {
			int truck = truck_weights[i];
            while(true) {
				// 큐에 아무것도 없는 경우 = 어떠한 트럭도 다리위에 없음 
				if(q.isEmpty()) { 
					q.add(truck);
					sum += truck;
                    answer++;
					break;
                }
                else if(q.size() == bridge_length) {
                    sum -= q.poll();
                }
                else  { // 다리 길이만큼 큐가 차지않았음
					// weight 값을 넘지 않는 선에서 새로운 트럭을 다리에 올려줌 
					if(sum + truck <= weight) {
						q.add(truck);
						sum += truck;
						answer++;
						break;
					} 
                    else { 
						// 넘는다면 0을 넣어 이미 큐에 있는 트럭이 다리를 건너게 만듬 
						q.add(0);
						answer++;
					}
                }
            }
        }
        return answer + bridge_length;
    }
}