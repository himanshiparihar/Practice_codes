int euclid(int a, int b)
{
	// do until the two numbers become equal
	while (a != b)
	{
		// replace larger number by its difference with the smaller number
		if (a > b)
			a = a - b;
		else
			b = b - a; 
	}

	return a;		// or b (since both are equal)
}