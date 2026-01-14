"""Triage Agent: ESI (Emergency Severity Index) Classification"""

import numpy as np
import pandas as pd
from typing import Dict, Tuple
import json

class TriageAgent:
    """
    Multi-agent system for patient triage using ESI protocol.
    Classifies patients into ESI levels 1-5 based on vital signs and chief complaint.
    
    ESI Levels:
    - Level 1: Requires immediate, life-saving intervention
    - Level 2: High-risk situation
    - Level 3: Stable, single resource needed
    - Level 4: Stable, single resource needed (simple)
    - Level 5: Stable, minimal resources needed
    """
    
    def __init__(self, confidence_threshold: float = 0.70):
        """
        Initialize the Triage Agent.
        
        Args:
            confidence_threshold: Minimum confidence to provide recommendation (default: 0.70)
        """
        self.confidence_threshold = confidence_threshold
        self.red_flags = {
            'respiratory_rate': (8, 30),  # breaths/min
            'heart_rate': (40, 130),  # bpm
            'systolic_bp': (90, 200),  # mmHg
            'temperature': (35, 40),  # Celsius
            'o2_saturation': (90, 100)  # %
        }
    
    def assess_vitals(self, vitals: Dict[str, float]) -> Tuple[str, float]:
        """
        Assess vital signs for critical abnormalities.
        
        Args:
            vitals: Dict with keys like 'respiratory_rate', 'heart_rate', etc.
        
        Returns:
            (esi_level, confidence): ESI level and confidence score
        """
        critical_flags = 0
        abnormal_flags = 0
        
        # Check for critical vital abnormalities
        for vital, (lower, upper) in self.red_flags.items():
            if vital in vitals:
                value = vitals[vital]
                if value < lower or value > upper:
                    abnormal_flags += 1
                    if value < lower * 0.5 or value > upper * 1.5:  # Very abnormal
                        critical_flags += 1
        
        # Determine ESI level based on vital abnormalities
        if critical_flags >= 2:
            esi_level = '1'  # Critical - immediate intervention
            confidence = 0.95
        elif abnormal_flags >= 3:
            esi_level = '2'  # High-risk
            confidence = 0.88
        elif abnormal_flags >= 1:
            esi_level = '3'  # Moderate
            confidence = 0.82
        else:
            esi_level = '4'  # Stable
            confidence = 0.79
        
        return esi_level, confidence
    
    def classify(self, patient_data: Dict) -> Dict:
        """
        Classify patient and provide triage recommendation.
        
        Args:
            patient_data: Dict with 'chief_complaint' and 'vitals'
        
        Returns:
            Dict with 'esi_level', 'confidence', 'reasoning', 'escalate'
        """
        chief_complaint = patient_data.get('chief_complaint', '').lower()
        vitals = patient_data.get('vitals', {})
        
        # Get ESI assessment from vitals
        esi_level, confidence = self.assess_vitals(vitals)
        
        # Check for life-threatening chief complaints
        critical_complaints = ['chest pain', 'difficulty breathing', 'severe bleeding', 
                               'unconscious', 'altered mental status', 'severe trauma']
        
        if any(complaint in chief_complaint for complaint in critical_complaints):
            esi_level = '1'
            confidence = 0.96
            reasoning = f"Critical chief complaint detected: {chief_complaint}"
        else:
            reasoning = f"Based on vital signs assessment: {esi_level}"
        
        # Determine if we should escalate to human
        should_escalate = confidence < self.confidence_threshold
        
        return {
            'esi_level': esi_level,
            'confidence': confidence,
            'reasoning': reasoning,
            'escalate': should_escalate,
            'recommendation': 'ESCALATE TO CLINICIAN' if should_escalate else f'ESI Level {esi_level}'
        }


# Example usage
if __name__ == '__main__':
    agent = TriageAgent(confidence_threshold=0.70)
    
    # Test case 1: Critical patient
    patient_1 = {
        'chief_complaint': 'Difficulty breathing',
        'vitals': {
            'respiratory_rate': 35,  # Abnormal
            'heart_rate': 120,  # Elevated
            'systolic_bp': 140,
            'temperature': 37.5,
            'o2_saturation': 88  # Low!
        }
    }
    
    result_1 = agent.classify(patient_1)
    print("Patient 1 (Critical):")
    print(json.dumps(result_1, indent=2))
    print()
    
    # Test case 2: Stable patient
    patient_2 = {
        'chief_complaint': 'Minor headache',
        'vitals': {
            'respiratory_rate': 16,
            'heart_rate': 72,
            'systolic_bp': 118,
            'temperature': 36.8,
            'o2_saturation': 98
        }
    }
    
    result_2 = agent.classify(patient_2)
    print("Patient 2 (Stable):")
    print(json.dumps(result_2, indent=2))
