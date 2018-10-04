/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package lab2;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author eduardo
 */
public class AlunoTest {
    
    public AlunoTest() {
    }
    
    @BeforeClass
    public static void setUpClass() {
    }
    
    @AfterClass
    public static void tearDownClass() {
    }
    
    @Before
    public void setUp() {
    }
    
    @After
    public void tearDown() {
    }

    /**
     * Test of cadastraLaboratorio method, of class Aluno.
     */
    @Test
    public void testCadastraLaboratorio_String() {
        System.out.println("cadastraLaboratorio");
        String nomeLaboratorio = "";
        Aluno instance = new Aluno();
        instance.cadastraLaboratorio(nomeLaboratorio);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of cadastraLaboratorio method, of class Aluno.
     */
    @Test
    public void testCadastraLaboratorio_String_int() {
        System.out.println("cadastraLaboratorio");
        String nomeLaboratorio = "";
        int cota = 0;
        Aluno instance = new Aluno();
        instance.cadastraLaboratorio(nomeLaboratorio, cota);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of consomeEspaco method, of class Aluno.
     */
    @Test
    public void testConsomeEspaco() {
        System.out.println("consomeEspaco");
        String nomeLaboratorio = "";
        int mbytes = 0;
        Aluno instance = new Aluno();
        instance.consomeEspaco(nomeLaboratorio, mbytes);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of liberaEspaco method, of class Aluno.
     */
    @Test
    public void testLiberaEspaco() {
        System.out.println("liberaEspaco");
        String nomeLaboratorio = "";
        int mbytes = 0;
        Aluno instance = new Aluno();
        instance.liberaEspaco(nomeLaboratorio, mbytes);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of atingiuCota method, of class Aluno.
     */
    @Test
    public void testAtingiuCota() {
        System.out.println("atingiuCota");
        String nomeLaboratorio = "";
        Aluno instance = new Aluno();
        boolean expResult = false;
        boolean result = instance.atingiuCota(nomeLaboratorio);
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }
    
}
