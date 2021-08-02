#include <stdio.h>
#include <string.h>

FILE *f;
char site[100], file[100], string[1000];
int link, i;
struct{
	char name[100], ip[100],cost[5];
}n[10];

void get_neighbors(){
	printf("Links? "); scanf("%d",&link);getchar();
	for(i=0;i<link;i++){
		printf("\nLink-%d\n",i+1);
		printf("Name : ");fgets(n[i].name,100-1,stdin);
		strtok(n[i].name,"\n");
		printf("IP : ");fgets(n[i].ip,100-1,stdin);
		strtok(n[i].ip,"\n");
		printf("Cost : ");fgets(n[i].cost,100-1,stdin);
		strtok(n[i].cost,"\n");
	}
}

void generate_conf(){
	strcpy(file,"");
	strcat(file,site);
	strcat(file,"\\nlsr-");
	strcat(file,site);
	strcat(file,".conf");
	
	f = fopen(file,"wb");
	fprintf(f,"general\n{\n  network /ndn/\n  site /idn/%s\n  router /%%C1.Router/router\n\n  lsa-refresh-time 1800\n\n  lsa-interest-lifetime 4\n  \n  sync-protocol psync\n\n  sync-interest-lifetime 60000\n\n  state-dir       /var/lib/nlsr\n}",site);
	fprintf(f,"\n\nneighbors\n{\n   hello-retries 3\n   \n   hello-timeout 1\n   \n   hello-interval  60\n\n  adj-lsa-build-interval 10\n\n  face-dataset-fetch-tries 3\n  \n  face-dataset-fetch-interval 3600\n");
	for(i=0;i<link;i++){
		fprintf(f,"\n\n  neighbor\n  {\n    name /ndn/idn/%s/%%C1.Router/router\n    face-uri  udp://%s\n    link-cost %s\n  }",n[i].name,n[i].ip,n[i].cost);
	}
	fprintf(f,"\n}\n\nhyperbolic\n{\n\n  state off\n  \n  radius   123.456\n  angle    1.45,2.36\n}\n\nfib\n{\n  max-faces-per-prefix 3\n  \n  routing-calc-interval 15\n  \n}");
	fprintf(f,"\n\nadvertising\n{\n\n  prefix /ndn/idn/%s/lab/ndn\n  \n}",site);
	fprintf(f,"\nsecurity\n{\n  validator\n  {\n    rule\n    {\n      id \"NLSR Hello Rule\"\n      for data\n      filter\n      {\n        type name\n        regex ^[^<nlsr><INFO>]*<nlsr><INFO><><>$\n      }\n      checker\n      {\n        type customized\n        sig-type ecdsa-sha256\n        key-locator\n        {\n          type name\n          hyper-relation\n          {\n            k-regex ^([^<KEY><nlsr>]*)<nlsr><KEY><>$\n            k-expand \\\\1\n            h-relation equal\n            p-regex ^([^<nlsr><INFO>]*)<nlsr><INFO><><>$\n            p-expand \\\\1\n          }\n        }\n      }\n    }\n\n    rule\n    {\n      id \"NLSR LSA Rule\"\n      for data\n      filter\n      {\n        type name\n        regex ^[^<nlsr><LSA>]*<nlsr><LSA>\n      }\n      checker\n      {\n        type customized\n        sig-type ecdsa-sha256\n        key-locator\n        {\n          type name\n          hyper-relation\n          {\n            k-regex ^([^<KEY><nlsr>]*)<nlsr><KEY><>$\n            k-expand \\\\1\n            h-relation equal\n            ; the last four components in the prefix should be <lsaType><seqNo><version><segmentNo>\n            p-regex ^<localhop>([^<nlsr><LSA>]*)<nlsr><LSA>(<>*)<><><><>$\n            p-expand \\\\1\\\\2\n          }\n        }\n      }\n    }\n\n    rule\n    {\n      id \"NLSR Hierarchy Exception Rule\"\n      for data\n      filter\n      {\n        type name\n        regex ^[^<KEY><%%C1.Router>]*<%%C1.Router>[^<KEY><nlsr>]*<KEY><><><>$\n      }\n      checker\n      {\n        type customized\n        sig-type ecdsa-sha256\n        key-locator\n        {\n          type name\n          hyper-relation\n          {\n            k-regex ^([^<KEY><%%C1.Operator>]*)<%%C1.Operator>[^<KEY>]*<KEY><>$\n            k-expand \\\\1\n            h-relation equal\n            p-regex ^([^<KEY><%%C1.Router>]*)<%%C1.Router>[^<KEY>]*<KEY><><><>$\n            p-expand \\\\1\n          }\n        }\n      }\n    }\n\n    rule\n    {\n      id \"NLSR Hierarchical Rule\"\n      for data\n      filter\n      {\n        type name\n        regex ^[^<KEY>]*<KEY><><><>$\n      }\n      checker\n      {\n        type hierarchical\n        sig-type ecdsa-sha256\n      }\n    }\n\n    trust-anchor\n    {\n      type file\n      file-name \"root.cert\"\n    }\n  }\n\n  prefix-update-validator\n  {\n    rule\n    {\n      id \"NLSR ControlCommand Rule\"\n      for interest\n      filter\n      {\n        type name\n        regex ^<localhost><nlsr><prefix-update>[<advertise><withdraw>]<><><>$\n      }\n      checker\n      {\n        type customized\n        sig-type ecdsa-sha256\n        key-locator\n        {\n          type name\n          regex ^([^<KEY><%%C1.Operator>]*)<%%C1.Operator>[^<KEY>]*<KEY><>$\n        }\n      }\n    }\n\n    rule\n    {\n      id \"NLSR Hierarchy Rule\"\n      for data\n      filter\n      {\n        type name\n        regex ^[^<KEY>]*<KEY><><><>$\n      }\n      checker\n      {\n        type hierarchical\n        sig-type ecdsa-sha256\n      }\n    }\n\n    trust-anchor\n    {\n      type file\n      file-name \"site.cert\"\n    }\n  }\n\n  ; cert-to-publish \"root.cert\"\n  cert-to-publish \"site.cert\"\n  cert-to-publish \"operator.cert\"\n  cert-to-publish \"router.cert\"\n}");
	fclose(f);
}

void generate_initial_script(){
	strcpy(file,"");
	strcat(file,site);
	strcat(file,"\\initial-");
	strcat(file,site);
	strcat(file,".sh");
	
	f=fopen(file,"wb");
	fprintf(f,"\nndnsec-key-gen /ndn/idn/%s > site.key\nndnsec-cert-gen -s /ndn/ site.key > site.cert\nndnsec-cert-install -f site.cert\n",site);
	fprintf(f,"\nndnsec-key-gen /ndn/idn/%s/%%C1.Operator/op > operator.key \nndnsec-cert-gen -s /ndn/idn/%s operator.key > operator.cert \nndnsec-cert-install -f operator.cert",site,site);
	fprintf(f,"\nndnsec-key-gen /ndn/idn/%s/%%C1.Router/router > router.key \nndnsec-cert-gen -s /ndn/idn/%s/%%C1.Operator/op router.key > router.cert \nndnsec-cert-install -f router.cert",site,site);
	fprintf(f,"\nsudo cp /usr/local/etc/ndn/nfd.conf.sample /usr/local/etc/ndn/nfd.conf");
	fclose(f);
}

void generate_run_script(){
	strcpy(file,"");
	strcat(file,site);
	strcat(file,"\\run-");
	strcat(file,site);
	strcat(file,".sh");
	
	f=fopen(file,"wb");
	fprintf(f,"\nnfd-start");
	for(i=0;i<link;i++){
		fprintf(f,"\nnfdc face create udp://%s",n[i].ip);
	}
	fprintf(f, "\nsudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-%s.conf",site);
	fclose(f);
}

void generate_stop_script(){
	strcpy(file,"");
	strcat(file,site);
	strcat(file,"\\stop-");
	strcat(file,site);
	strcat(file,".sh");
	
	f=fopen(file,"wb");
	for(i=0;i<link;i++){
		fprintf(f,"\nnfdc face destroy udp://%s",n[i].ip);
	}
	fprintf(f,"\nnfd-start");
	fclose(f);
}

int main(){
	system("cls");
	printf("Site : "); fgets(site, 100-1, stdin);
	strtok(site,"\n");
	int check;
    char* dirname = site;
    check = mkdir(dirname,0777);
	get_neighbors();
	generate_conf();
	generate_initial_script();
	generate_run_script();
	generate_stop_script();
	char conf;
	fflush(stdin);
	printf("DONE!\nContinue?(y/n) ");
	scanf("%c",&conf);
	fflush(stdin);
	if(conf=='y'){
		main();
	}else{
		system("exit");
	}
}
