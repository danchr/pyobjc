import Security
from PyObjCTools.TestSupport import TestCase


class TestCSSMAPI(TestCase):
    def test_unsuppported(self):
        self.assertFalse(hasattr(Security, "CSSM_Init"))
        self.assertFalse(hasattr(Security, "CSSM_Terminate"))
        self.assertFalse(hasattr(Security, "CSSM_ModuleLoad"))
        self.assertFalse(hasattr(Security, "CSSM_ModuleUnload"))
        self.assertFalse(hasattr(Security, "CSSM_Introduce"))
        self.assertFalse(hasattr(Security, "CSSM_Unintroduce"))
        self.assertFalse(hasattr(Security, "CSSM_ModuleAttach"))
        self.assertFalse(hasattr(Security, "CSSM_ModuleDetach"))
        self.assertFalse(hasattr(Security, "CSSM_SetPrivilege"))
        self.assertFalse(hasattr(Security, "CSSM_GetPrivilege"))
        self.assertFalse(hasattr(Security, "CSSM_GetModuleGUIDFromHandle"))
        self.assertFalse(hasattr(Security, "CSSM_GetSubserviceUIDFromHandle"))
        self.assertFalse(hasattr(Security, "CSSM_ListAttachedModuleManagers"))
        self.assertFalse(hasattr(Security, "CSSM_GetAPIMemoryFunctions"))
        self.assertFalse(hasattr(Security, "CSSM_CSP_CreateSignatureContext"))
        self.assertFalse(hasattr(Security, "CSSM_CSP_CreateSymmetricContext"))
        self.assertFalse(hasattr(Security, "CSSM_CSP_CreateDigestContext"))
        self.assertFalse(hasattr(Security, "CSSM_CSP_CreateMacContext"))
        self.assertFalse(hasattr(Security, "CSSM_CSP_CreateRandomGenContext"))
        self.assertFalse(hasattr(Security, "CSSM_CSP_CreateAsymmetricContext"))
        self.assertFalse(hasattr(Security, "CSSM_CSP_CreateDeriveKeyContext"))
        self.assertFalse(hasattr(Security, "CSSM_CSP_CreateKeyGenContext"))
        self.assertFalse(hasattr(Security, "CSSM_CSP_CreatePassThroughContext"))
        self.assertFalse(hasattr(Security, "CSSM_GetContext"))
        self.assertFalse(hasattr(Security, "CSSM_FreeContext"))
        self.assertFalse(hasattr(Security, "CSSM_SetContext"))
        self.assertFalse(hasattr(Security, "CSSM_DeleteContext"))
        self.assertFalse(hasattr(Security, "CSSM_GetContextAttribute"))
        self.assertFalse(hasattr(Security, "CSSM_UpdateContextAttributes"))
        self.assertFalse(hasattr(Security, "CSSM_DeleteContextAttributes"))
        self.assertFalse(hasattr(Security, "CSSM_CSP_Login"))
        self.assertFalse(hasattr(Security, "CSSM_CSP_Logout"))
        self.assertFalse(hasattr(Security, "CSSM_CSP_GetLoginAcl"))
        self.assertFalse(hasattr(Security, "CSSM_CSP_ChangeLoginAcl"))
        self.assertFalse(hasattr(Security, "CSSM_GetKeyAcl"))
        self.assertFalse(hasattr(Security, "CSSM_ChangeKeyAcl"))
        self.assertFalse(hasattr(Security, "CSSM_GetKeyOwner"))
        self.assertFalse(hasattr(Security, "CSSM_ChangeKeyOwner"))
        self.assertFalse(hasattr(Security, "CSSM_CSP_GetLoginOwner"))
        self.assertFalse(hasattr(Security, "CSSM_CSP_ChangeLoginOwner"))
        self.assertFalse(hasattr(Security, "CSSM_SignData"))
        self.assertFalse(hasattr(Security, "CSSM_SignDataInit"))
        self.assertFalse(hasattr(Security, "CSSM_SignDataUpdate"))
        self.assertFalse(hasattr(Security, "CSSM_SignDataFinal"))
        self.assertFalse(hasattr(Security, "CSSM_VerifyData"))
        self.assertFalse(hasattr(Security, "CSSM_VerifyDataInit"))
        self.assertFalse(hasattr(Security, "CSSM_VerifyDataUpdate"))
        self.assertFalse(hasattr(Security, "CSSM_VerifyDataFinal"))
        self.assertFalse(hasattr(Security, "CSSM_DigestData"))
        self.assertFalse(hasattr(Security, "CSSM_DigestDataInit"))
        self.assertFalse(hasattr(Security, "CSSM_DigestDataUpdate"))
        self.assertFalse(hasattr(Security, "CSSM_DigestDataClone"))
        self.assertFalse(hasattr(Security, "CSSM_DigestDataFinal"))
        self.assertFalse(hasattr(Security, "CSSM_GenerateMac"))
        self.assertFalse(hasattr(Security, "CSSM_GenerateMacInit"))
        self.assertFalse(hasattr(Security, "CSSM_GenerateMacUpdate"))
        self.assertFalse(hasattr(Security, "CSSM_GenerateMacFinal"))
        self.assertFalse(hasattr(Security, "CSSM_VerifyMac"))
        self.assertFalse(hasattr(Security, "CSSM_VerifyMacInit"))
        self.assertFalse(hasattr(Security, "CSSM_VerifyMacUpdate"))
        self.assertFalse(hasattr(Security, "CSSM_VerifyMacFinal"))
        self.assertFalse(hasattr(Security, "CSSM_QuerySize"))
        self.assertFalse(hasattr(Security, "CSSM_EncryptData"))
        self.assertFalse(hasattr(Security, "CSSM_EncryptDataP"))
        self.assertFalse(hasattr(Security, "CSSM_EncryptDataInit"))
        self.assertFalse(hasattr(Security, "CSSM_EncryptDataInitP"))
        self.assertFalse(hasattr(Security, "CSSM_EncryptDataUpdate"))
        self.assertFalse(hasattr(Security, "CSSM_EncryptDataFinal"))
        self.assertFalse(hasattr(Security, "CSSM_DecryptData"))
        self.assertFalse(hasattr(Security, "CSSM_DecryptDataP"))
        self.assertFalse(hasattr(Security, "CSSM_DecryptDataInit"))
        self.assertFalse(hasattr(Security, "CSSM_DecryptDataInitP"))
        self.assertFalse(hasattr(Security, "CSSM_DecryptDataUpdate"))
        self.assertFalse(hasattr(Security, "CSSM_DecryptDataFinal"))
        self.assertFalse(hasattr(Security, "CSSM_QueryKeySizeInBits"))
        self.assertFalse(hasattr(Security, "CSSM_GenerateKey"))
        self.assertFalse(hasattr(Security, "CSSM_GenerateKeyP"))
        self.assertFalse(hasattr(Security, "CSSM_GenerateKeyPair"))
        self.assertFalse(hasattr(Security, "CSSM_GenerateKeyPairP"))
        self.assertFalse(hasattr(Security, "CSSM_GenerateRandom"))
        self.assertFalse(hasattr(Security, "CSSM_CSP_ObtainPrivateKeyFromPublicKey"))
        self.assertFalse(hasattr(Security, "CSSM_WrapKey"))
        self.assertFalse(hasattr(Security, "CSSM_UnwrapKey"))
        self.assertFalse(hasattr(Security, "CSSM_WrapKeyP"))
        self.assertFalse(hasattr(Security, "CSSM_UnwrapKeyP"))
        self.assertFalse(hasattr(Security, "CSSM_DeriveKey"))
        self.assertFalse(hasattr(Security, "CSSM_FreeKey"))
        self.assertFalse(hasattr(Security, "CSSM_GenerateAlgorithmParams"))
        self.assertFalse(hasattr(Security, "CSSM_CSP_GetOperationalStatistics"))
        self.assertFalse(hasattr(Security, "CSSM_GetTimeValue"))
        self.assertFalse(hasattr(Security, "CSSM_RetrieveUniqueId"))
        self.assertFalse(hasattr(Security, "CSSM_RetrieveCounter"))
        self.assertFalse(hasattr(Security, "CSSM_VerifyDevice"))
        self.assertFalse(hasattr(Security, "CSSM_CSP_PassThrough"))
        self.assertFalse(hasattr(Security, "CSSM_TP_SubmitCredRequest"))
        self.assertFalse(hasattr(Security, "CSSM_TP_RetrieveCredResult"))
        self.assertFalse(hasattr(Security, "CSSM_TP_ConfirmCredResult"))
        self.assertFalse(hasattr(Security, "CSSM_TP_ReceiveConfirmation"))
        self.assertFalse(hasattr(Security, "CSSM_TP_CertReclaimKey"))
        self.assertFalse(hasattr(Security, "CSSM_TP_CertReclaimAbort"))
        self.assertFalse(hasattr(Security, "CSSM_TP_FormRequest"))
        self.assertFalse(hasattr(Security, "CSSM_TP_FormSubmit"))
        self.assertFalse(hasattr(Security, "CSSM_TP_CertGroupVerify"))
        self.assertFalse(hasattr(Security, "CSSM_TP_CertCreateTemplate"))
        self.assertFalse(hasattr(Security, "CSSM_TP_CertGetAllTemplateFields"))
        self.assertFalse(hasattr(Security, "CSSM_TP_CertSign"))
        self.assertFalse(hasattr(Security, "CSSM_TP_CrlVerify"))
        self.assertFalse(hasattr(Security, "CSSM_TP_CrlCreateTemplate"))
        self.assertFalse(hasattr(Security, "CSSM_TP_CertRevoke"))
        self.assertFalse(hasattr(Security, "CSSM_TP_CertRemoveFromCrlTemplate"))
        self.assertFalse(hasattr(Security, "CSSM_TP_CrlSign"))
        self.assertFalse(hasattr(Security, "CSSM_TP_ApplyCrlToDb"))
        self.assertFalse(hasattr(Security, "CSSM_TP_CertGroupConstruct"))
        self.assertFalse(hasattr(Security, "CSSM_TP_CertGroupPrune"))
        self.assertFalse(hasattr(Security, "CSSM_TP_CertGroupToTupleGroup"))
        self.assertFalse(hasattr(Security, "CSSM_TP_TupleGroupToCertGroup"))
        self.assertFalse(hasattr(Security, "CSSM_TP_PassThrough"))
        self.assertFalse(hasattr(Security, "CSSM_AC_AuthCompute"))
        self.assertFalse(hasattr(Security, "CSSM_AC_PassThrough"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CertCreateTemplate"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CertGetAllTemplateFields"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CertSign"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CertVerify"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CertVerifyWithKey"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CertGetFirstFieldValue"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CertGetNextFieldValue"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CertAbortQuery"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CertGetKeyInfo"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CertGetAllFields"))
        self.assertFalse(hasattr(Security, "CSSM_CL_FreeFields"))
        self.assertFalse(hasattr(Security, "CSSM_CL_FreeFieldValue"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CertCache"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CertGetFirstCachedFieldValue"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CertGetNextCachedFieldValue"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CertAbortCache"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CertGroupToSignedBundle"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CertGroupFromVerifiedBundle"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CertDescribeFormat"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CrlCreateTemplate"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CrlSetFields"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CrlAddCert"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CertGetKeyInfo"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CertGetAllFields"))
        self.assertFalse(hasattr(Security, "CSSM_CL_FreeFields"))
        self.assertFalse(hasattr(Security, "CSSM_CL_FreeFieldValue"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CertCache"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CertGetFirstCachedFieldValue"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CertGetNextCachedFieldValue"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CertAbortCache"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CertGroupToSignedBundle"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CertGroupFromVerifiedBundle"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CertDescribeFormat"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CrlCreateTemplate"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CrlSetFields"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CrlAddCert"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CrlRemoveCert"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CrlSign"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CrlVerify"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CrlVerifyWithKey"))
        self.assertFalse(hasattr(Security, "CSSM_CL_IsCertInCrl"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CrlGetFirstFieldValue"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CrlGetNextFieldValue"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CrlAbortQuery"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CrlGetAllFields"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CrlCache"))
        self.assertFalse(hasattr(Security, "CSSM_CL_IsCertInCachedCrl"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CrlGetFirstCachedFieldValue"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CrlGetNextCachedFieldValue"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CrlGetAllCachedRecordFields"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CrlAbortCache"))
        self.assertFalse(hasattr(Security, "CSSM_CL_CrlDescribeFormat"))
        self.assertFalse(hasattr(Security, "CSSM_CL_PassThrough"))
        self.assertFalse(hasattr(Security, "CSSM_DL_DbOpen"))
        self.assertFalse(hasattr(Security, "CSSM_DL_DbClose"))
        self.assertFalse(hasattr(Security, "CSSM_DL_DbCreate"))
        self.assertFalse(hasattr(Security, "CSSM_DL_DbDelete"))
        self.assertFalse(hasattr(Security, "CSSM_DL_CreateRelation"))
        self.assertFalse(hasattr(Security, "CSSM_DL_DestroyRelation"))
        self.assertFalse(hasattr(Security, "CSSM_DL_Authenticate"))
        self.assertFalse(hasattr(Security, "CSSM_DL_GetDbAcl"))
        self.assertFalse(hasattr(Security, "CSSM_DL_ChangeDbAcl"))
        self.assertFalse(hasattr(Security, "CSSM_DL_GetDbOwner"))
        self.assertFalse(hasattr(Security, "CSSM_DL_ChangeDbOwner"))
        self.assertFalse(hasattr(Security, "CSSM_DL_GetDbNames"))
        self.assertFalse(hasattr(Security, "CSSM_DL_GetDbNameFromHandle"))
        self.assertFalse(hasattr(Security, "CSSM_DL_FreeNameList"))
        self.assertFalse(hasattr(Security, "CSSM_DL_DataInsert"))
        self.assertFalse(hasattr(Security, "CSSM_DL_DataDelete"))
        self.assertFalse(hasattr(Security, "CSSM_DL_DataModify"))
        self.assertFalse(hasattr(Security, "CSSM_DL_DataGetFirst"))
        self.assertFalse(hasattr(Security, "CSSM_DL_DataGetNext"))
        self.assertFalse(hasattr(Security, "CSSM_DL_DataAbortQuery"))
        self.assertFalse(hasattr(Security, "CSSM_DL_DataGetFromUniqueRecordId"))
        self.assertFalse(hasattr(Security, "CSSM_DL_FreeUniqueRecord"))
        self.assertFalse(hasattr(Security, "CSSM_DL_PassThrough"))
