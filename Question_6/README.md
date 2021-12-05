
Question 6 Terraform:<br>
=====================<br>

Table of Content:<br>

Creating the Q_6_TF project.<br>
Fig 1.1: After creating Q_6_TF.tf file, populating the config with nano.<br>
Fig 1.2: Initializing the populated TF project and validating the file.<br>
Fig 1.3: The instance is created in TF from the local VM.<br>
Fig 1.4: Instance i-0b7093992caaede47 is created on AWS and visible on the web portal.<br>

Creating variables.<br>
Fig 2.1: Updated the AMI in the Q_6_TF.tf file. Changes were applied.<br>
Fig 2.2: Modified region field to region = var.region.<br>
Fig 2.3: Receiving error messages.<br>
Fig 2.4: Refreshed Terraform config and the previous instance was terminated.<br>
Instance i-094aa05bdcb352fd2 was created. Created and modified variables.tf.<br>
Fig 2.5: Changes reflected in AWS Instances.<br>
Fig 2.6: Output of "terraform graph" of the latest i-094aa05bdcb352fd2 instance.<br>
Fig 2.7: Updated Q_6_TF.tf file.<br>
Fig 2.8: Updated variables.tf file.<br>

Outputs.tf and Displaying IP.<br>
Fig 3.1: Created outs.tf file.<br>
Fig 3.2: Refreshed config, output is displayed at the last step after applied the new config.<br>
Fig 3.3: Running terraform output command on local VM.<br>
Fig 3.4: AWS displays the latest instance with the IP address for cross-reference.<br>
