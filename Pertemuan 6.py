{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyMN3jk/IYtoD38fjegKQjRa"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":null,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"lek2qFh4TPKc","executionInfo":{"status":"ok","timestamp":1730378277975,"user_tz":-420,"elapsed":851,"user":{"displayName":"Dela Nurain","userId":"06323738407539544349"}},"outputId":"be59a3f0-d3c1-4e1e-ae32-ba2485e2b6bd"},"outputs":[{"output_type":"stream","name":"stdout","text":["100\n","951\n","651\n","69\n","319\n","601\n","485\n","507\n","725\n","547\n","615\n","83\n","165\n","141\n","501\n","263\n","617\n","865\n","575\n","219\n","105\n","941\n","47\n","907\n","375\n","823\n","597\n","615\n","953\n","345\n","399\n","219\n","237\n","949\n","687\n","217\n","815\n","67\n","767\n","553\n"]}],"source":["\n","numbers = [\n"," 951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725,\n","547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390,\n","984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236,\n","375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219,\n","918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815,\n","67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,\n","742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440,\n","380, 126, 721, 328, 753, 470, 743, 527\n","]\n","\n","\n","print(len(numbers))\n","i = 0\n","while i < len(numbers):\n","    if numbers[i] % 2 ==1:\n","      print(numbers[i])\n","    if numbers[i] == 553:\n","      break\n","    i+=1"]},{"cell_type":"code","source":["#Buatlah output dari menggunakan bahasa pemrograman python dengan:\n","\n","jumlah=0\n","string=\"\"\n","for i in range(1,20,2):\n","  jumlah += i\n","  string += f\"{i}\"\n","  if i == 19 :\n","    string +=\"=\"\n","  else:\n","    string +=\"+\"\n","print(f\"{string} {jumlah}\")"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"-fBCV8Lb6rro","executionInfo":{"status":"ok","timestamp":1730267110219,"user_tz":-420,"elapsed":1545,"user":{"displayName":"Dela Nurain","userId":"06323738407539544349"}},"outputId":"70f3fad7-c8f5-492d-e2fa-400f7f092def"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["1+3+5+7+9+11+13+15+17+19= 100\n"]}]},{"cell_type":"code","source":["jumlah_baris =int(input(\"masukan jumlah baris\"))\n","for i in range(1, jumlah_baris +1):\n","         print(\"*\" * i)"],"metadata":{"id":"dHSGGq0KlTpi","executionInfo":{"status":"ok","timestamp":1730442864915,"user_tz":-420,"elapsed":9580,"user":{"displayName":"Dela Nurain","userId":"06323738407539544349"}},"outputId":"c30c6926-0001-4e59-9e33-1adc4a8159c5","colab":{"base_uri":"https://localhost:8080/"}},"execution_count":1,"outputs":[{"output_type":"stream","name":"stdout","text":["masukan jumlah baris20\n","*\n","**\n","***\n","****\n","*****\n","******\n","*******\n","********\n","*********\n","**********\n","***********\n","************\n","*************\n","**************\n","***************\n","****************\n","*****************\n","******************\n","*******************\n","********************\n"]}]}]}