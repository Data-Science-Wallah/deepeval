import os
import pandas as pd
from deepeval.metrics import (
    AnswerRelevancyMetric,
    ContextualPrecisionMetric,
    ContextualRelevancyMetric,
    HallucinationMetric,
)
from deepeval.test_case import LLMTestCase


def test_answer_relevancy():
    # Path to your Excel file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, "deepeval_rag_test.xlsx")
    output_file = os.path.join(current_dir, "deepeval_rag_test_results.xlsx")
    
    print(f"Reading from: {input_file}")
    
    try:
        # Read the Excel file
        df = pd.read_excel(input_file)
        print(f"Successfully loaded Excel with {len(df)} rows")
        
        # Create metrics
        arm = AnswerRelevancyMetric(threshold=0.7)
        cr = ContextualRelevancyMetric(threshold=0.7)
        cp = ContextualPrecisionMetric(threshold=0.7)
        hm = HallucinationMetric(threshold=0.7)
        
        # Process each row in the Excel file
        for index, row in df.iterrows():
            print(f"Processing row {index+1}/{len(df)}")
            
            # Convert retrieval_context and context to list if they're strings
            retrieval_context = row['retrieval_context']
            if isinstance(retrieval_context, str):
                retrieval_context = [retrieval_context]
                
            context = row['context']
            if isinstance(context, str):
                context = [context]
                
            # Create test case
            test_case = LLMTestCase(
                input=row['input'],
                actual_output=row['actual_output'],
                expected_output=row['expected_output'],
                retrieval_context=retrieval_context,
                context=context,
            )
            
            # Run metrics
            arm.measure(test_case)
            cr.measure(test_case)
            cp.measure(test_case)
            hm.measure(test_case)
            
            # Update DataFrame with scores
            df.at[index, 'answer_relevancy_score'] = arm.score
            df.at[index, 'contextual_relevancy_score'] = cr.score
            df.at[index, 'contextual_precision_score'] = cp.score
            df.at[index, 'hallucination_score'] = hm.score
            
            print(f"Row {index+1} scores: AR={arm.score:.2f}, CR={cr.score:.2f}, CP={cp.score:.2f}, H={hm.score:.2f}")
        
        # Save updated DataFrame to a new Excel file
        df.to_excel(output_file, index=False)
        print(f"Results successfully saved to {output_file}")
        
    except Exception as e:
        print(f"Error processing Excel file: {str(e)}")
        import traceback
        print(traceback.format_exc())


if __name__ == "__main__":
    test_answer_relevancy()
