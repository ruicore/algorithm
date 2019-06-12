'use strict'


var length=3;//内存中页面的最大长度
var resource=[];//分配内存空间
var times=[];//下一次访问时，记录每个页面从载入到当前经过的单位时间个数
var i=0;

for (i=0;i<length+2;i++)
{
    resource.push(-1);//初始化已分配的资源为-1，表示当前还没有资源
}
for (i=0;i<length;i++)
{
    times.push(0);//初始化到当前为止所有资源已在内存中停留的单位之间个数，为0，表示停留时间为0及还没有分配资源；
}


	//------------------一下为测试输出----------------------
var list=[7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1];
var j=0;
for (i=0;i<20;i++)
{
    LRU_PageReplacement(resource,times, length, list[i]);
    console.log(resource);//输出当前资源的分配情况
   // console.log(times);//输出资源在内存中的停留单位时间状况
}


//保持和FIFO的接口风格一致，增添了times参数，来记录上次使用的次数，因此resource里面的标识符由原来的三位变成两位

function LRU_PageReplacement(resource,times,length,page_num)
{
    var i=0,j=0;
    var max=0,max_pos=0;

    for (i=2;i<length+2;i++)
    {
        if (page_num == resource[i])//表示请求的页面在已经分配的内存中
		{
			resource[0] = 0;//0表示不需要请求新的页面
			resource[1] = i;//请求的页面在第i号位置
			times[i - 2] = 1;//记录请求的页面的在内存中的次数重置为1
			for (j = 0; j < length; j++)//循环遍历内存中页面的停留次数
			{
				if (times[j] == 0)//如果该位置的停留次数为0，表示该位置还从来没有被分配过页面，跳过
					continue;
				if (j == i - 2)
					continue;//分配内存对应的记录次数的位置，重置为1，表示下一次请求时，该页面已经在内存中停留了一次
				else 
					times[j] += 1;//其余位置依次增加1个停留时间
			}

			return;
		}
    }
    //请求的页面不在已分配的内存中
	max = times[0];
	for (j = 0; j < length; j++)//找到停留最久的页面在内存中的位置
	{
		if (times[j] == 0)//如果该位置还没有被分配过，则直接分配
		{
			max_pos = j;
			break;
		}
		if (times[j] > max)
		{
			max = times[j];
			max_pos = j;
		}
	}

	resource[max_pos + 2] = page_num;
	resource[0] = 1;
	resource[1] = max_pos + 2;
	times[max_pos] = 1;

	for (j = 0; j < length; j++)//循环遍历内存中页面的停留次数
	{
		if (times[j] == 0)//如果该位置的停留次数为0，表示该位置还从来没有被分配过页面，跳过
			continue;
		if (j == max_pos)
			continue;//分配内存对应的记录次数的位置，重置为1，表示下一次请求时，该页面已经在内存中停留了一次
		else
			times[j] += 1;//其余位置依次增加1个停留时间
	}

	return;
}
