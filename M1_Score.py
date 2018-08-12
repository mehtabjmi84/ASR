import argparse
import wer
# create a function that calls wer.string_edit_distance() on every utterance
# and accumulates the errors for the corpus. Then, report the word error rate (WER)
# and the sentence error rate (SER). The WER should include the the total errors as well as the
# separately reporting the percentage of insertions, deletions and substitutions.
# The function signature is
# num_tokens, num_errors, num_deletions, num_insertions, num_substitutions = wer.string_edit_distance(ref=reference_string, hyp=hypothesis_string)
#
def score(ref_trn=None, hyp_trn=None):
    
    
    
    t_sen=0
    t_esen=0
    t_w=0
    t_i=0
    t_d=0
    t_s=0
    t_e=0
    with open(ref_trn) as f1, open(hyp_trn) as f2:
        for x, y in zip(f1, f2):
            x=x.split()
            y=y.split()
            #try:
            #    x.remove('')
            #    y.remove('')
            #except:
            #    pass
            
            num_tokens, num_errors, num_deletions, num_insertions, num_substitutions = wer.string_edit_distance(ref=x, hyp=y)
            print("Id:"+str(x[len(x)-1])+"Scores: N=%i ,S=%i ,D=%i ,I=%i"%(num_tokens-1,num_substitutions,num_deletions, num_insertions))
            print("  ")
            t_sen=t_sen+1
            if num_errors>0:
                t_esen=t_esen+1
            t_w=t_w+num_tokens-1
            t_d=t_d+num_deletions
            t_s=t_s+num_substitutions
            t_i=t_i+num_insertions
            t_e=t_e+num_errors
    
    
    
    
    
    
    print("Sentence Error Rate:")
    print("Sum:  N=%i  ,Error Sentences=%i" %(t_sen,t_esen))
    print("Average:  N=%i  ,Error precentage=%f" %(t_sen,(t_esen/t_sen)*100))
    
    print("Word Error Rate:")
    print("Sum:  N=%i  ,Total Error=%i, Substitution=%i, Deletion=%i, Insertion=%i" %(t_w,t_e,t_s,t_d,t_i))
    print("Average:  N=%i  ,Error precentage=%f,Subs. Error precentage=%f,Del. Error precentage=%f,Inser. Error precentage=%f" %(t_w,(t_e/t_w)*100,(t_s/t_w)*100,(t_d/t_w)*100,(t_i/t_w)*100))
    
    
    


    return


if __name__=='__main__':
    parser = argparse.ArgumentParser(description="Evaluate ASR results.\n"
                                                "Computes Word Error Rate and Sentence Error Rate")
    
    parser.add_argument('-ht','--hyptrn', help='Hypothesized transcripts in TRN format', required=True, default=None)
    parser.add_argument('-rt','--reftrn', help='Reference transcripts in TRN format', required=True, default=None)

    args = parser.parse_args()

    if args.reftrn is None or args.hyptrn is None:
        RuntimeError("Must specify reference trn and hypothesis trn files.")
    

    score(ref_trn=args.reftrn, hyp_trn=args.hyptrn)
