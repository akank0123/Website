<!DOCTYPE html>
<html>
 
<head>
</head>
 
<body>
    <center>
        <?php


        $servername = "localhost";
        $username = "root";
        $password = "empty";
        $databasename = "dataform";
        $conn = mysqli_connect("localhost", "root", "", "dataform");
        
        // Check connection
        if($conn === false){
            die("ERROR: Could not connect. "
                . mysqli_connect_error());
        }
        
        // Taking all 4 values from the form data(input)
        $city = $_REQUEST['city'];
        $datajob = $_REQUEST['datajob'];
        $experience = $_REQUEST['experience'];
        $phone = $_REQUEST['phone'];
        $laptop = $_REQUEST['laptop'];
        $work = $_REQUEST['work'];
        $joining = $_REQUEST['joining'];
        $rate = $_REQUEST['rate'];
        $office = $_REQUEST['office'];
        $language = $_REQUEST['language'];
        
        // Performing insert query execution
        // here our table name is data
        $sql = "INSERT INTO data VALUES ('$id','$city', '$datajob' , '$experience' , '$phone' , '$laptop' , '$work' , '$joining'
            '$rate','$office','$language')";
        
        if(mysqli_query($conn, $sql)){
            echo "<h3>data stored in a database successfully."
                . " Please browse your localhost php my admin"
                . " to view the updated data</h3>";

            // echo nl2br("\n$name\n $date\n "
            //     . "$intime\n $outtime");
        } else{
            echo "ERROR: Hush! Sorry $sql. "
                . mysqli_error($conn);
        }
        
        // Close connection
        mysqli_close($conn);
        ?>
     </center>
</body>
</html>
