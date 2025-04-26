property fifo_no_overflow(clk, rst_n, wr_ptr[3:0], rd_ptr[3:0]);
@(posedge clk)
disable iff !rst_n (wr_ptr[2:0] == rd_ptr[2:0]) ->(wr_ptr[3] !== rd_ptr[3]) ;
endproperty

FIFO_NO_OVERFLOW: assert fifo_no_overflow(clk, rst_n, wr_ptr, rd_ptr);

//Function to return -1 if element is not found.
//Else returns the index of the element within the array
function int binary_sort(int an_element,ref input int an_array[]);
binary_sort = -1;
if(an_element >= an_array[0] && )


endfunction