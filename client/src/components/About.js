import {useState, useEffect} from 'react'
import Slideshow from './Slideshow'


function About(){

    const images = [
            '/images/0F14C30A-DFCA-4E7D-80D1-DC475DDFC953.jpeg',
            '/images/1F8104A9-2AF0-48F5-8A71-967A72F7259D.jpeg',
            '/images/2BD2D144-4C18-42C1-9C35-461FBC0ACAE5_1_105_c.jpeg',
            '/images/2D2FA7D3-1A5C-4A13-93C8-F436F29DAE54.jpeg',
            '/images/03D91329-AA63-4EA0-B57D-DDBE9B455558_1_105_c.jpeg',
            '/images/4A3B8D60-9C37-4F59-ADAF-8E65D521B141.jpeg',
            '/images/4D69577A-4C74-4BB9-B740-BB0BF73D50FD_1_105_c.jpeg',
            '/images/4E40C4ED-0341-45CF-A38D-CC051830D84B.jpeg',
            '/images/4F4A3C9E-D65C-4272-9FE7-33814870784B.jpeg',
            '/images/5CC61138-24E9-4E92-8D74-366E576AC2DF.jpeg',
            '/images/5F886DEC-B55D-47DE-84D1-24D6C30885D2.jpeg',
            '/images/5F3524C6-8729-4C2B-B758-C4148F727AD4.jpeg',
            '/images/6CB75F0D-15F1-4F21-A9C6-D686FE855DBE_1_105_c.jpeg',
            '/images/6E7F67EA-F132-4990-BB4C-465B49A8F1EC_1_105_c.jpeg',
            '/images/7A8AB514-8005-4C18-9864-695AECC096C2.jpeg',
            '/images/7E2BC2F5-59EF-442E-9459-644CEA412954.jpeg',
            '/images/8E7873B7-3D7F-4A50-8307-FD80B2A087F0.jpeg',
            '/images/8FAC8FA4-8EB5-4B7C-A2FA-E9F8BD903B1C.jpeg',
            '/images/9A03535C-EA23-4F1E-97CD-BEE80D45811B_1_105_c.jpeg',
            '/images/9CAAF8E0-F871-4746-97BF-49316EB622CA_1_105_c.jpeg',
            '/images/09ED6C73-124B-4F97-9399-96249FF47DC5_1_105_c.jpeg',
            '/images/27D4AF3A-9C8D-4587-9859-AE222A2A5491.jpeg',
            '/images/34EA8ECC-CB9B-417C-9143-969549DC8AC5_1_105_c.jpeg',
            '/images/35EF3EB2-B8D4-4E8C-9E34-7BBE52FD622D.jpeg',
            '/images/043F4999-49F1-40C7-88D6-39238980AF84.jpeg',
            '/images/45E1A283-8044-4F83-A64D-C388D1D9C736.jpeg',
            '/images/84C69B87-76CB-406A-8023-48C06FB76235.jpeg',
            '/images/91D53DB8-D37E-43B1-85EA-697148265880.jpeg',
            '/images/97B14951-FF4B-4C2F-9F8C-D7270197D055.jpeg',
            '/images/418F76FD-A8A3-4E77-8192-3DD056E85492.jpeg',
            '/images/558E64B6-F9D4-476A-BFAA-0045ED7CBE0E.jpeg',
            '/images/652A215C-3134-4746-AE44-E2202C6DB5FC_1_105_c.jpeg',
            '/images/659B359F-3BF0-4F99-A13E-8BC7794AF14D_1_105_c.jpeg',
            '/images/670B6C90-7A53-41F6-9217-9D2095503248.jpeg',
            '/images/717E0090-320E-441F-BB26-9E82EC3C432C.jpeg',
            '/images/808B1E0D-33B0-4465-9D3A-C5E6937E0D45.jpeg',
            '/images/857B9847-51C5-4426-B158-43BE7870318C_1_105_c.jpeg',
            '/images/889BD21C-4046-4F2A-AC4B-26262808B6AC_1_105_c.jpeg',
            '/images/1607D910-89A2-4A72-9D65-25211FB2413C.jpeg',
            '/images/04071A34-CDB0-4D9E-B19B-75C475BAE4B1.jpeg',
            '/images/378777BD-3D7D-4982-BD25-32629108E077.jpeg',
            '/images/693635A6-146C-406C-842E-20C4F0CFFC7B.jpeg',
            '/images/A7765120-6005-4139-8091-AFCD92F06017.jpeg',
            '/images/about.jpg',
            '/images/AED8BABF-BC65-42BF-90DE-77E53ED95422.jpeg',
            '/images/AFE99ADE-D318-4343-BEC0-C8347E4EFF4F.jpeg',
            '/images/B71B37C8-570F-441D-A0FC-5541995B54FE.jpeg',
            '/images/B9182D8D-26DA-483B-A853-8594C3D3B79A_1_105_c.jpeg',
            '/images/B4764630-4E35-4CDE-83E0-486172667CE1.jpeg',
            '/images/B9018618-5AF9-4676-8F35-9C25CE1CB3B3.jpeg',
            '/images/C65F777D-1037-49C2',
          
    ]

    return(
        <div>
            {/* <img className = 'about-image' src="../images/about.jpg"></img> */}
            <Slideshow images={images} />
            <p className = 'about-description'>
            Daphna and Chuchu have a love for food that is relatable for your average foodie... maybe your extreme foodie. They are home-chefs, but skilled ones at that. Over the years they have compiled and adapted recipes from their childhoods, online, and even invented a few of their own. These recipes are meant to be home recipes and can be made by any and all! This book began as a family google drive that Daphna and Chuchu made for their children, so that we can always make a meal that reminds us of them. So if you’re reading this it means that the Friedlanders have allowed this website to be published. 
                <br></br>
                <br></br>
            These recipes cover a large range of cuisines and might appear to be randomly mixed together, but you should know that if it has made it into this ‘book’ it has been eaten and enjoyed many times in the Friedlander household. You’ll also notice that there are some categories that are specific to Jewish holidays, in those categories there are some family staples that we look forward to enjoying every year (some passed down from generations…). 
            <br></br>
            <br></br>
            We hope these recipes bring you as much joy as they have to us. In many ways this is a heartwarming legacy left by Daphna and Chuchu. Their children and their grandchildren will make these meals and always remember Daphna and Chuchu’s dinner table fondly.
            </p>
        </div>
)}

export default About