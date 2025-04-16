interface ShotData {
    playerId: number;
    distance: number;
    period: number;
    //add more features as needed    
  }
  
  interface PredictionResult {
    successProbability: number; // (0-1)
    confidenceInterval?: [number, number]; 
    contributingFactors?: {     
      [factor: string]: number; // Factor name and its weight
    }; 
    similarHistoricalShots?: {  	// Similar shots from historical data
      count: number;
      madePercentage: number;
      examples: Array<{
        playerId: number;
        playerName: string;
        gameId: string;
        wasSuccessful: boolean;
      }>;
    };
  }
  class NBAModelClient {
    private baseUrl: string;   
    constructor(baseUrl: string = 'http://localhost:5000') {
      this.baseUrl = baseUrl;
    }
   
    async predictShot(data: ShotData): Promise<PredictionResult> {
      try {
        const response = await fetch(`${this.baseUrl}/predict`, {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify(data)
        });
        
        if (!response.ok) {
          throw new Error(`API error: ${response.status}`);
        }
        
        return await response.json();
      } catch (error) {
        console.error('Prediction failed:', error);
        throw error;
      }
    }
  }
  
  
  
  
  