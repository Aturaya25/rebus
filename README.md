# rebus
Decipher the record of an arithmetic equality in which digits are replaced by letters, and different digits are replaced by different letters, the same ones are replaced by the same letters. It is assumed that the original equality is correct and written according to the usual rules of arithmetic. In particular, in the record of the number the first digit on the left is not the digit 0; the decimal number system is used. Enter the rebus in the format ЧИСЛО+ЕЩЕ=СУММА, output all solutions in string lexicographical order in a column.

***For example***

***1)***

*input*

     ТРУД+ВОЛЯ=УДАЧА
     
*output*

      4612+7893=12505
      4812+7693=12505
      5312+7496=12808
      5412+7396=12808
      5614+8709=14323
      5714+8609=14323
      6514+7809=14323
      6814+7509=14323
      7312+5496=12808
      7412+5396=12808
      7514+6809=14323
      7612+4893=12505
      7812+4693=12505
      7814+6509=14323
      8614+5709=14323
      8714+5609=14323
      
***2)***      

*input*

      КОКА+КОЛА=ВОДА
      
*output*

      3930+3980=7910
