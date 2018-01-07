void array_sum(int a[], int b[], int c[], int size) {
	int i, ans, q;
  	ans = 0;
  	q = 0;
  	for(i = 0; i < size; i++)    
	{
    	c[i] = a[i] + b[i] + q;
    	ans = c[i];
    	q = ans / 10;
    	if (c[i] >= 10)
    	{
    	  c[i] = c[i] % 10;
    	}
    	else 
    	{ 
    	  c[i] = c[i];  
    	}
	}
  return;
}
